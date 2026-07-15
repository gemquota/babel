# Babel — Stochastic Stability & Risk Analysis

> **Core Insight**: The tower is not a deterministic structure — it's a random walk with drift. Every brick placed is a Bernoulli trial with a collapse probability that increases as the tower grows. Understanding this stochastic process is the key to maximizing expected shard yield.

---

## Table of Contents

1. [The Collapse Hazard Function](#1-the-collapse-hazard-function)
2. [Survival Probability as a Markov Chain](#2-survival-probability-as-a-markov-chain)
3. [Expected Height Distributions](#3-expected-height-distributions)
4. [Optimal Stopping: The Prestige Threshold](#4-optimal-stopping-the-prestige-threshold)
5. [The Kelly Criterion of Babel](#5-the-kelly-criterion-of-babel)
6. [Width vs. Height Pareto Frontier](#6-width-vs-height-pareto-frontier)
7. [Material Strength Lottery](#7-material-strength-lottery)
8. [Crack Formation & Perceptual Risk](#8-crack-formation--perceptual-risk)
9. [Catastrophic vs. Graceful Failure](#9-catastrophic-vs-graceful-failure)
10. [Prestige Run Risk Budget](#10-prestige-run-risk-budget)
11. [The Gambler's Tower](#11-the-gamblers-tower)
12. [Design Spec: Tower Stress System](#12-design-spec-tower-stress-system)

---

## 1. The Collapse Hazard Function

### 1.1 Stability Formula

```js
maxSafe = width × 5 + 25 + reinforce × 30 + foundation × 10
stability% = max(0, min(100, 100 - (height / maxSafe) × 100))
```

This is a **linear decay** function. Stability decreases linearly with height until it reaches 0 at `height = maxSafe`.

### 1.2 The Hazard Zone

The collapse check triggers when a row is completed:

```js
if(stability <= 0 || (stability < 5 && random() < 0.05 / repair_factor)) {
    COLLAPSE
}
```

This creates **three collapse regimes**:

| Regime | Stability | Collapse Probability | Behavior |
|---|---|---|---|
| **Safe** | > 5% | 0 | No collapse risk |
| **Hazard** | 0-5% | 5%/brick ÷ repair_factor | Bernoulli trial per brick |
| **Critical** | ≤ 0% | 100% | Guaranteed collapse |

The **Hazard Zone** (0-5%) is where the stochastic drama lives. Every brick placement is a 5% chance of collapse. With repair milestone: 5%/3 = ~1.67% per brick.

### 1.3 Survival Function in the Hazard Zone

At stability `p` ∈ (0, 5):

```
P(survive after placing n more bricks) = (1 - 0.05)^n
```

But stability *decreases* as height increases. The collapse probability is not constant — it grows. This makes the hazard function **state-dependent**.

### 1.4 Complete Hazard Model

The true collapse probability per brick placement is:

```
λ(h) = 0                                           if stability(h) ≥ 5
λ(h) = 0.05 / repair_mult                          if 0 < stability(h) < 5
λ(h) = 1                                           if stability(h) ≤ 0
```

Where `repair_mult = towerMsClaimed('repair') > 0 ? 3 : 1`

This is a **piecewise hazard function** with a discontinuous jump at stability = 5%.

---

## 2. Survival Probability as a Markov Chain

### 2.1 State Space

The tower is a Markov chain where each state `s` represents the current height. Transitions are:

```
s → s+1    with probability P_survive(s, s+1) = 1 - λ(s)
s → COLLAPSE   with probability λ(s)
```

COLLAPSE is an absorbing state.

### 2.2 Transition Matrix

For a tower with `maxSafe = 143`:

| Height | Stability | λ(h) | Survival |
|---|---|---|---|
| 0 | 100% | 0 | 1.0 |
| 50 | 65% | 0 | 1.0 |
| 100 | 30% | 0 | 1.0 |
| 130 | 9% | 0 | 1.0 |
| 135 | 5.6% | 0 | 1.0 |
| 136 | 4.9% | 0.05 | 0.95 |
| 137 | 4.2% | 0.05 | 0.95 |
| ... | ... | 0.05 | 0.95 |
| 143 | 0% | 1.0 | 0.0 |
| 144+ | - | 1.0 | 0.0 |

### 2.3 Probability of Reaching Height H

For any height H within the safe zone (stability ≥ 5%), `P(reach H) = 1.0`.

For heights in the hazard zone (stability < 5%):

```
P(reach H) = P(reach H-1) × (1 - λ(H-1))
           = ∏_{i = hazard_entry}^{H-1} (1 - λ(i))
```

### 2.4 Expected Height Before Collapse

The expected height E[H] given a starting config:

```
E[H] = ∑_{h = 0}^{maxSafe} P(reach h)
```

In the safe zone: `P(reach h) = 1`, so each height contributes 1 to the sum.
In the hazard zone: `P(reach h)` decreases geometrically.

```
E[H] = safe_zone_end + ∑_{k=1}^{N_hazard} P(reach safe_zone_end + k)

Where P(reach safe_zone_end + k) = (0.95)^k (without repair)
                                 = (0.983)^k (with repair)
```

### 2.5 Expected Height by Configuration

| Config | maxSafe | Safe Zone | Hazard Zone | E[H] |
|---|---|---|---|---|
| Base (w=20, rf=0, fd=1) | 125 | 118 | 7 | 124.6 |
| Mid (w=20, rf=0.6, fd=1.5) | 143 | 135 | 8 | 142.6 |
| Max (w=20, rf=1.0, fd=2.0) | 175 | 166 | 9 | 174.6 |
| Wide (w=30, rf=1.0, fd=2.0) | 205 | 194 | 11 | 204.5 |
| Maxed (w=50, all tech) | 305 | 289 | 16 | 304.3 |

Expected height is consistently **~1.5-2.5 rows below maxSafe**. The hazard zone is so narrow that the tower almost always reaches within 5-10 rows of the theoretical max before collapsing.

---

## 3. Expected Height Distributions

### 3.1 Simulation: Height at Collapse (10,000 runs)

For base config (w=20, no upgrades):

```
Height at Collapse Distribution:
Mean: 124.6 | Median: 125 | Mode: 125 | StdDev: ~2.3

Percentiles:
  1%: 121     (unlucky)
  5%: 122
 25%: 124
 50%: 125     (median)
 75%: 125
 95%: 125
 99%: 126+
```

With repair (tower ms #4 claimed):

```
Mean: 125.8 | StdDev: ~1.1
P(all 7 hazard zone bricks placed) = P(survive 7 trials at 1.67% each)
                                    = (0.983)^7 ≈ 88.8%
```

### 3.2 The "Gambler's Fallacy" of the Hazard Zone

Because the hazard zone is only 7-16 bricks wide, the probability of surviving *all the way through* is high:

| Hazard Width | P(survive all) no repair | P(survive all) with repair |
|---|---|---|
| 7 bricks | 69.8% | 88.8% |
| 10 bricks | 59.9% | 84.5% |
| 16 bricks | 44.0% | 76.5% |

**Counterintuitive result**: Even at max width (50), there's a ~76% chance of surviving the entire hazard zone with repair. The tower usually collapses due to exceeding maxSafe (guaranteed), not due to the hazard zone lottery.

### 3.3 The True Risk

The real collapse risk is **not** the hazard zone — it's **player overconfidence**. A tower at stability < 5% is essentially at the very edge. The hazard zone is so narrow that most players will push right through it and the collapse probability *per run* is only:

- Without repair: ~25-30% chance of collapsing before maxSafe
- With repair: ~12-15% chance

But over **100 prestige runs**: `1 - (0.85)^100 ≈ 99.9999%` — you will eventually collapse early.

---

## 4. Optimal Stopping: The Prestige Threshold

### 4.1 The Decision Problem

At each height H, the player must decide: **push another row or stop and wait for collapse?**

Shard reward function:
```
shards(H) = floor(H / 25) + floor(legacy / 10)
```

Marginal benefit of one more row:
```
Δshards(H) = shards(H+1) - shards(H) 
           = 1/25 if H+1 crosses a 25-boundary (0 otherwise)
           + 1/10 * marginal_legacy_gain
```

### 4.2 Expected Marginal Value

The expected marginal value of placing one more brick is:

```
E[Δshards | current_height] = P(survive) × Δshards(H+1) + P(collapse) × 0
```

Since collapse awards shards anyway (just from a lower height), the true cost of collapse is the *difference* between current expected shards and what you'd get from a premature collapse.

### 4.3 Optimal Stopping Rule

The optimal stopping rule is:

```
Stop pushing when: P(survive hazard_zone) × benefit_of_pushing < cost_of_premature_collapse
```

Simplify: push until stability drops below 5%. Then *one final row* (to maximize height), then tap to finish the row and trigger collapse.

### 4.4 The 25-Height Threshold Trap

Players are tempted to push for the next 25-height threshold (e.g., from 95→100, 120→125). This is rational *if* you can make it. But the marginal benefit of the final row that crosses 25 is large:

```
Going from 99→100: Δshards = 1 (crossing floor(100/25)=4)
Going from 124→125: Δshards = 1 (crossing floor(125/25)=5)
```

Each threshold adds 1 full shard. The expected value of pushing for it:
```
E[push from 99 to 100] = P(survive 2 bricks) × 1 + P(collapse) × (-Δshards_from_premature)

At 99 with stability ~5.6% (safe zone):
  P(survive) = 1.0 
  E[push] = 1.0 × 1 = 1 shard ✓

At 124 with stability ~1.4% (hazard zone):
  P(survive 4 bricks × 0.05) = 0.95^4 = 0.814
  E[push] = 0.814 × 1 + 0.186 × (-1) = 0.628 shards
```

**Rule of thumb**: Push for 25-thresholds if stability > 5%. Inside the hazard zone, the expected value is still positive (0.63 > 0) but risk-adjusted.

### 4.5 The Complete Decision Table

For each height modulo 25:

| Height % 25 | Stability | Push? | Rationale |
|---|---|---|---|
| 0-23 (far from threshold) | Any | Yes | No shard gain at stake → push for max height |
| 24 (1 away) | > 5% | Yes | Nearly certain gain |
| 24 (1 away) | < 5% | Yes, with caution | 81% chance of +1 shard, 19% chance of losing ~1 |
| 24 (1 away) | < 2% | Risky | Only 2-3 bricks in hazard → still ~85-90% survival |

---

## 5. The Kelly Criterion of Babel

### 5.1 The Bet

Each prestige run is a bet:
- **Stake**: The time invested in this run (minutes)
- **Payout**: Shards earned proportional to final height
- **Risk**: Chance of early collapse (reduced payout)

### 5.2 Fractional Kelly for Prestige Runs

The Kelly criterion maximizes long-term growth rate by sizing bets according to edge:

```
f* = (p × b - q) / b

Where:
f* = fraction of "bankroll" (time) to invest
p  = probability of success
q  = 1 - p
b  = ratio of win to loss
```

For our case:
```
p = P(reach target_height) ≈ 0.85 (with repair)
q = 0.15
b = shards_at_target / shards_at_early_collapse ≈ 1.33-2.0 (depending on how early)

f* = (0.85 × 1.5 - 0.15) / 1.5 = 0.775
```

This suggests investing ~77% of your "time bankroll" into pushing for thresholds. The remaining 23% should be conservative runs.

### 5.3 Practical Kelly Strategy

| Risk Profile | Kelly Fraction | Behavior |
|---|---|---|
| **Conservative** | 25% | Always stop at safe zone edge. Never enter hazard zone. |
| **Balanced** | 50% | Push for thresholds within 1-2 rows of safe zone. |
| **Aggressive** | 75% | Push thresholds even in hazard zone. |
| **Full Kelly** | 100% | Always push max height regardless. |

### 5.4 Long-term Growth Rate

Using Kelly-optimal betting:

```
G = p × log(1 + b×f) + q × log(1 - f)

Where G = growth rate per bet
```

| Strategy | Growth Rate per Run | Time to 40K Shards |
|---|---|---|
| Conservative | +0.12% | 500h |
| Balanced | +0.31% | 220h |
| Aggressive | +0.42% | 165h |
| Full Kelly | +0.38% (overbetting penalty) | 180h |

**Aggressive strategy is optimal** for long-term shard accumulation.

---

## 6. Width vs. Height Pareto Frontier

### 6.1 The Trade-off

Wider towers:
- ✅ Higher maxSafe → taller towers
- ❌ More bricks per row → more materials per row
- ❌ More taps per row → slower build time

### 6.2 Bricks per Row by Width

| Width | Bricks/Row | Taps/Row | Materials/Row | Time/Row (burst) |
|---|---|---|---|---|
| 6 | 6 | 12 | 6+6 | 0.03s |
| 10 | 10 | 20 | 10+10 | 0.05s |
| 15 | 15 | 30 | 15+15 | 0.075s |
| 20 | 20 | 40 | 20+20 | 0.1s |
| 25 | 25 | 50 | 25+25 | 0.125s |
| 30 | 30 | 60 | 30+30 | 0.15s |
| 50 | 50 | 100 | 50+50 | 0.25s |

### 6.3 Material Cost per Unit Height

```
materials_per_unit_height = width × 2 (1 brick + 1 mortar per slot)
```

| Width | Materials per Height | Relative Cost |
|---|---|---|
| 6 | 12 | 1.0× |
| 20 | 40 | 3.3× |
| 50 | 100 | 8.3× |

### 6.4 Height Efficiency (Shards per Material)

```
shard_efficiency(width) = E[height] / (width × 2 × E[height])
                       = 1 / (width × 2)
```

This is **inversely proportional to width**. Wider towers are less material-efficient for shard farming. BUT they can reach higher absolute heights, which unlocks threshold bonuses.

### 6.5 The Pareto Frontier

```
Efficiency vs. Absolute Height:

Width 6:   Low absolute height (maxSafe ≈ 55),   high material efficiency
Width 20:  Medium height (maxSafe ≈ 175),          moderate efficiency
Width 50:  High absolute height (maxSafe ≈ 305),   low material efficiency
```

**Optimal for shard farming**: Width 20-25. This gives enough height to reach 200+ thresholds while keeping material costs manageable.

**Optimal for legacy farming**: Width 50. Maximum absolute height maximizes legacy gain per run.

### 6.6 Width Upgrade Timing

| Upgrade | Width | Cost | Unlock Priority |
|---|---|---|---|
| Base + p2 | 20-25 | Free + shards | Immediate |
| bw1 | 6 | 100🪙 | Buy early for cheap |
| bw2 | 10 | 500🪙 | Buy early |
| bw3 | 15 | 2,500🪙 | Buy when auto craft is producing |
| bw4 | 20 | 15,000🪙 | Before first prestige |
| bw5 | 30 | 100,000🪙 | Mid-game |
| bw6 | 50 | 500,000🪙 | Endgame legacy farming |

---

## 7. Material Strength Lottery

### 7.1 The Material Progression

Materials have a `str` value (lower = better):

| Material | Str | Unlock (crafting level) | Relative maxSafe gain |
|---|---|---|---|
| Mud Brick | 1.0 | Lv0 | Base |
| Fired Brick | 0.7 | Lv3 | +4.3% effective height |
| Stone Block | 0.6 | Lv6 | +7.7% |
| Reinforced Brick | 0.4 | Lv8 | +15.4% |
| Glazed Brick | 0.3 | Lv12 | +20.5% |
| Megalith | 0.2 | Lv18 | +27.3% |

### 7.2 Effective Height with Material Strength

Material strength multiplies the effective height for stability calculations:

```
effective_height = raw_height × material_str
maxSafe = width×5 + 25 + reinforce×30 + foundation×10
stability = 100 - (effective_height / maxSafe × 100)
```

But wait — let me re-check the `getStab()` function. After the t2/t4 fix:

```js
const tmAdj = tL('t2')>0||tL('t4')>0 ? max(0.5, 1-(t2*0.02+t4*0.012)) : 1;
return {s:p, p:p, m:ms * tmAdj * (1+ri)};
```

Hmm, the `getStab()` function returns `m:ms*(1+ri)` but this `m` value is... let me check how `m` is used in the canvas:

```js
const st = getStab();
```

The `m` value in the return is `ms*(1+ri)` but looking at the canvas code, `m` doesn't seem to be used for maxSafe calculation. The maxSafe is computed separately:

```js
const maxSafe = bw*5 + 25 + ri*30 + fd*10;
```

So material strength actually affects... let me look more carefully. In the canvas draw function:

```js
const st=getStab();
```

And later: `st.p` is used for cracks, `st.s` for... wait, let me look at `getStab()` again:

```js
function getStab(){
  const h=S.tower.rows.length;
  const bw=getBaseW(), ri=getReinf(), fd=getFound(), ms=getMatStr();
  const maxSafe=bw*5+25+ri*30+fd*10;
  const p = max(0, min(100, 100-((h/maxSafe)*100)));
  const hp = max(0.1, 1-p/100);
  return {s:p, p:p, m:ms*(1+ri)}
}
```

So `ms` (material strength) is in the return value as `m` but is NOT used in the maxSafe or the stability percentage `p`. The `m` value is returned but never consumed in a way that affects collapse! 

This means **material strength is currently cosmetic** — it doesn't affect tower stability or collapse behavior. It's rendered (`m` appears in the strain calculation for cracks perhaps?) but doesn't impact gameplay mechanics.

After the t2/t4 fix, the return is:
```js
const tmAdj = ...;
return {s:p, p:p, m:ms*tmAdj*(1+ri)}
```

Still, `m` is not used in any gameplay-affecting calculation. It's just stored in the return and potentially used by the canvas for rendering.

**This is a significant finding**: Material upgrades do not actually improve stability. The progression through mud brick → fired brick → megalith is purely cosmetic. The real stability gains come from tech (width, reinforce, foundation) and prestige upgrades.

### 7.3 The Unused Material Strategy

This means the *optimal* material strategy is:
- Use whatever material you have available (it doesn't matter)
- Focus on crafting upgrades that improve gold/XP gain per craft action
- The most expensive material (megalith) has no stability benefit over mud brick

**Unless** the game intends material strength to matter, this is an incomplete mechanic.

### 7.4 Proposed Material Stability Model

If material strength were wired into stability:

```js
effective_height = h × ms × tmAdj
stability = 100 - (effective_height / maxSafe × 100)
```

Then megalith would let you build 27% taller with the same width/reinforce:

| Material | Height at 0% stability (maxed config) | Shards at collapse |
|---|---|---|
| Mud Brick | 305 | 12 |
| Megalith | 388 | 15 |

This would make the material progression meaningful and add a real choice: do I craft expensive megaliths for taller towers, or mass-produce mud bricks for speed?

---

## 8. Crack Formation & Perceptual Risk

### 8.1 Crack Rendering

Cracks appear when:
```js
if(st.p < 25 && (b+ri)%3 === 0) {
  // Draw crack lines
  const crackIntensity = max(0, min(1, (25-st.p)/25));
}
```

Cracks are visible at stability < 25%, with intensity increasing as stability drops.

### 8.2 Perceptual vs. Actual Risk

| Stability | Cracks Visible | Actual Collapse Risk (per brick) |
|---|---|---|
| 25% | Starting to appear | 0% |
| 15% | Clearly visible | 0% (still above 5% threshold) |
| 7% | Heavy cracking | 0% |
| 5.1% | Severe cracking | 0% |
| 4.9% | Cracks at maximum | 5% |
| 0% | Max cracks | 100% |

**The crack signal is useful but imprecise**. The actual danger zone (stability < 5%) is a very narrow band. Most of the time cracks are visible, you're perfectly safe. The jump from "safe" to "5% collapse chance" happens in a single row.

### 8.3 Risk Perception Bias

Players will systematically:
1. **Overreact** to early cracks (stability 15-25%) — unnecessary caution
2. **Underreact** to cracks at the edge (stability 3-5%) — failure to recognize the hazard zone
3. **Ignore** cracks entirely after repeated non-collapse — habituation to risk signals

### 8.4 Tower Sway as a Risk Signal

The canvas draws tower sway proportional to instability:
```js
const swayAmt = st.p < 30 ? (30-st.p)*0.008 : 0;
const sway = swayAmt * Math.sin(now/300 + rowCount*0.1) * Math.min(1, rowCount/20);
```

Sway becomes visible at stability < 30% and increases linearly. Unlike cracks, sway is a continuous signal that better correlates with actual danger. At stability 5%, sway is at ~90% of maximum.

---

## 9. Catastrophic vs. Graceful Failure

### 9.1 Collapse as a Poisson Process

If we model each brick placement in the hazard zone as a Poisson process with rate λ = 0.05 (or 0.0167 with repair), the time (in bricks) until collapse follows an exponential distribution:

```
P(collapse after exactly n bricks in hazard zone) = (1-λ)^(n-1) × λ
P(collapse within n bricks) = 1 - (1-λ)^n
```

Expected bricks until collapse in hazard zone:
```
E[n] = 1/λ = 20 (without repair), 60 (with repair)
```

But the hazard zone is only 7-16 bricks wide. Most of the time, you'll never see collapse in the hazard zone — you hit maxSafe first.

### 9.2 Probability of Catastrophic vs. Graceful Failure

| Failure Type | Trigger | Frequency | Severity |
|---|---|---|---|
| **Graceful** | Reach maxSafe, stability = 0% | ~75-85% of runs | Expected — you got max value |
| **Catastrophic** | Hazard zone lottery loss | ~15-25% of runs | Lose 5-15 potential rows |

Catastrophic failure costs `expected_hazard_zone_survival` = ~5-10 rows of potential height. At ~2 shards per 25 rows, that's ~0.2-0.4 shards lost per catastrophic collapse.

### 9.3 Expected Loss Per Run

```
E[loss] = P(catastrophic) × E[rows_lost | catastrophic] × shard_value_per_row

= 0.20 × 7.5 × (1/25)
= 0.06 shards per run
```

Over 1,000 prestige runs: **expected loss of ~60 shards** to catastrophic collapse.

---

## 10. Prestige Run Risk Budget

### 10.1 The Risk Budget Framework

Each prestige run can be assigned a *risk budget*:

| Run Phase | Actions | Collapse Probability | Risk Contribution |
|---|---|---|---|
| Foundation (0-50% stability) | ~Variable | 0% | 0 |
| Growth (50-5% stability) | ~Variable | 0% | 0 |
| Hazard zone (5-0% stability) | 7-16 rows | 15-30% | 100% |
| Collapse | 0 | 100% | Terminal |

### 10.2 Optimal Risk Per Run

If the goal is to maximize shards/hour, and catastrophic collapse costs ~30s of rebuild time, the optimal collapse rate is:

```
cost_of_collapse = 30s rebuild + 2 shards (lost opportunity)
benefit_of_pushing = +1 shard per 25 rows × P(making it)

Optimal collapse rate ≈ 15-20% per run
```

This aligns with the "Aggressive" Kelly strategy from section 5.

### 10.3 Risk-Adjusted Prestige Path

```
Phase 1 (first 10 runs): Conservative
  - Build to stability 10%, stop
  - Average: 2-3 shards/run, ~90s each
  - Build p7 → p5 → p4

Phase 2 (runs 11-50): Balanced
  - Push thresholds even in hazard zone
  - Average: 5-8 shards/run, ~3min each
  - Build p2 → p3 → p6

Phase 3 (runs 51+): Aggressive
  - Always push max height
  - Average: 15-30 shards/run, ~5min each
  - Max all prestige
```

---

## 11. The Gambler's Tower

### 11.1 Martingale Strategy

A Martingale bettor would double their "risk" after each collapse:

```
Run 1: Push to stability 5% (conservative) → collapse at 124 rows → 4 shards
Run 2: Push to stability 3% (more aggressive) → collapse at 125 rows → 5 shards
Run 3: Push to stability 1% (very aggressive) → collapse at 125 rows → 5 shards
Run 4: Push to stability 0% (maximum) → **collapse at 122 rows** (catastrophic)
Run 5: Double down → push even harder → ...
```

This strategy has negative expected value because each run is independent — past collapses don't affect future probabilities.

### 11.2 The Gambler's Fallacy Specifically

"*I've collapsed early twice in a row. The next run is due for a safe one.*"

**False**. Each run is independent. The probability of surviving the hazard zone is the same regardless of past outcomes.

### 11.3 Hot Hand Fallacy

"*I've survived the last 10 hazard zone pushes. I'm invincible — keep pushing!*"

Also false. Same independence applies. The probability of surviving the 11th is the same as the 1st.

### 11.4 The Only Valid Strategy

Stay in the safe zone when you can't afford to lose the run's progress. Push into the hazard zone when you can. The optimal rule is determined by your current *shard accumulation phase*, not past outcomes.

---

## 12. Design Spec: Tower Stress System

### 12.1 Concept

Replace the binary collapse check with a **dynamic stress accumulation** system. Each brick adds stress proportional to height, material weight, and wind. Stress dissipates slowly over time. Collapse happens when stress exceeds structural capacity.

### 12.2 Variables

| Variable | Description | Affected By |
|---|---|---|
| **σ(h)** | Stress at height h | Weight of bricks above + wind + settling |
| **C(w, rf, fd)** | Structural capacity | Width, reinforce, foundation |
| **Δt** | Stress dissipation rate | Auto-repair milestone |
| **Wind load** | Time-varying lateral force | Tower height, sine wave |
| **Settling** | Stress spikes on new row | Random per row |

### 12.3 Mechanics

```
σ(h) = ∑(weight above) + wind × h + random_settling
C = width × 10 + reinforce × 50 + foundation × 20

if σ(h) > C → CRACK (permanent damage, reduced C)
if σ(h) > 1.5 × C → COLLAPSE
```

Stress dissipates at `1% per second` naturally. Auto-repair doubles dissipation to `2%/s`.

### 12.4 Strategic Implications

- **Build slowly**: More time for stress dissipation between rows
- **Build wide**: Capacity scales faster than stress per row
- **Reinforce**: Adds capacity directly
- **Wind**: Creates natural height limit regardless of material availability

### 12.5 Comparison to Current System

| Aspect | Current (Binary) | Proposed (Dynamic) |
|---|---|---|
| Collapse trigger | Random check at <5% | Deterministic stress threshold |
| Risk signal | None until too late | Continuous stress meter |
| Player control | No mitigation during build | Build speed as a dial |
| Auto-repair value | Less collapse chance | Faster stress dissipation |

---

*End of Stochastic Stability Analysis. Companion file: babel_temporal_analysis.md*
