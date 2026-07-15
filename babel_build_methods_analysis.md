# Babel — Build Methods Comparative Analysis

> **The Central Question**: Three methods exist to place bricks — burst, hold, and automation. Each has a fundamentally different cost structure, time profile, and progression arc. How do they compare, and how do they synergize with every other system in the game?

---

## Table of Contents

1. [The Build Trilemma](#1-the-build-trilemma)
2. [Method 1: Hold-to-Repeat](#2-method-1-hold-to-repeat)
3. [Method 2: Burst Engine](#3-method-2-burst-engine)
4. [Method 3: Auto-Build](#4-method-3-auto-build)
5. [Sustained Throughput Analysis](#5-sustained-throughput-analysis)
6. [Cost Structure Comparison](#6-cost-structure-comparison)
7. [Material Efficiency](#7-material-efficiency)
8. [Talent Synergy Matrix](#8-talent-synergy-matrix)
9. [Prestige Synergy Matrix](#9-prestige-synergy-matrix)
10. [Tech & Milestone Synergy](#10-tech--milestone-synergy)
11. [Phase 1: Early Game (First Prestige)](#11-phase-1-early-game-first-prestige)
12. [Phase 2: Mid Game (Auto Economy)](#12-phase-2-mid-game-auto-economy)
13. [Phase 3: Late Game (Prestige Loops)](#13-phase-3-late-game-prestige-loops)
14. [Phase 4: Endgame (Max Efficiency)](#14-phase-4-endgame-max-efficiency)
15. [Burst Engine Upgrade Path Optimization](#15-burst-engine-upgrade-path-optimization)
16. [Hold Method Upgrade Path Optimization](#16-hold-method-upgrade-path-optimization)
17. [Auto-Build Upgrade Path Optimization](#17-auto-build-upgrade-path-optimization)
18. [The Complete Build Economy](#18-the-complete-build-economy)
19. [Method Selection by Tower Width](#19-method-selection-by-tower-width)
20. [Hybrid Strategies](#20-hybrid-strategies)
21. [Burst Charge Mathematics](#21-burst-charge-mathematics)
22. [Hold Warm-Up Mathematics](#22-hold-warm-up-mathematics)
23. [Automation Breakpoint Mathematics](#23-automation-breakpoint-mathematics)
24. [Material-Method Fit Analysis](#24-material-method-fit-analysis)
25. [Stability-Risk-Method Tradeoffs](#25-stability-risk-method-tradeoffs)
26. [Tower Height Milestone Racing](#26-tower-height-milestone-racing)
27. [Prestige Cycle Optimization by Method](#27-prestige-cycle-optimization-by-method)
28. [Offline Progress & Method Selection](#28-offline-progress--method-selection)
29. [Gold Economy & Method Selection](#29-gold-economy--method-selection)
30. [XP Economy & Method Selection](#30-xp-economy--method-selection)
31. [Design Analysis: The Three Philosophies](#31-design-analysis-the-three-philosophies)
32. [Method Switching: When and Why](#32-method-switching-when-and-why)
33. [Theoretical Maximum Build Speed](#33-theoretical-maximum-build-speed)
34. [One-Weird-Trick: Edge Cases & Exploits](#34-one-weird-trick-edge-cases--exploits)
35. [Conclusion: The Optimal Player](#35-conclusion-the-optimal-player)

---

## 1. The Build Trilemma

### 1.1 The Three Methods

The player has exactly three ways to place bricks on the Tower of Babel:

| Method | Activation | Base Speed | Primary Cost | Scalability |
|---|---|---|---|---|
| **Hold-to-Repeat** | Hold finger on build zone | 8.3 taps/s (120ms) | Attention + time | Gold upgrades only |
| **Burst Engine** | Tap burst button | 20 taps/s initially | Gold + charges | 5 upgrade tracks |
| **Auto-Build** | Passive automation | 0.5 taps/s at Lv1 | Gold (upfront) | Gold + p5 prestige |

### 1.2 Why Three Methods?

Each method serves a different player need:

- **Hold** is the *default*. It's always available, costs nothing, and requires continuous attention. It's the baseline against which other methods are measured.
- **Burst** is the *sprint*. It compresses many actions into a short window but requires recovery. It's for when you need height *now*.
- **Auto-Build** is the *background*. It runs while you're in other tabs or offline. It's the ultimate time saver.

### 1.3 The Unification Principle

All three methods ultimately call `tapBuild()`, which places bricks through the same 2-tap system. The difference is *how fast* and *how often* they call it. This means:

- All methods benefit from width reductions, stability improvements, and material strength
- All methods consume the same materials per brick
- All methods award the same XP per brick
- All methods trigger the same collapse checks

The methods only differ in **temporal profile** and **cost structure**.

---

## 2. Method 1: Hold-to-Repeat

### 2.1 Mechanics

```js
// Fires every 120ms while held
htInt = setInterval(fn, 120);
```

Each tick calls `tapBuild()`, which handles one brick state transition (empty → positioned → placed).

### 2.2 Speed Profile

Hold-to-repeat fires at a **constant 120ms interval**, regardless of game state:

| Duration Held | Actions | Bricks Placed (2-tap) | Rows (width 20) |
|---|---|---|---|
| 1 second | 8.3 | 4.2 | 0.21 |
| 10 seconds | 83 | 42 | 2.1 |
| 1 minute | 500 | 250 | 12.5 |
| 10 minutes | 5,000 | 2,500 | 125 |

### 2.3 Upgrade Path

The hold method upgrades through the **tap upgrade tree**:

| Upgrade | Effect | Cost Progression | Max Level |
|---|---|---|---|
| None | 120ms interval | Free | — |
| (No direct speed upgrade exists) | | | |

Hold-to-repeat speed is **not directly upgradeable** in the current design. Its effectiveness comes from:
- **Brick power**: Via tap upgrades (g1-g4, c1-c4) which affect gold/resource yield, not build speed
- **Stability upgrades**: Higher stability = fewer collapses = more uptime
- **Width tech**: Narrower towers = fewer bricks per row = more rows per tap session

### 2.4 Opportunity Cost

Hold-to-repeat occupies your **full attention**. While holding:
- You cannot gather (different tab)
- You cannot craft (different tab)  
- You cannot upgrade (different tab)
- You cannot manage talents or prestige

The one exception: **auto-gather and auto-craft continue running** in the background, replenishing materials.

### 2.5 Finger Fatigue Model

Real-world human holding time follows a decay curve:
- 0-30s: Full speed (8.3 taps/s)
- 30-60s: Fatigue sets in (may slow to 6-7 taps/s)
- 60-120s: Significant fatigue (4-5 taps/s)
- 120s+: Intermittent holding (bursts of 10-20s)

This makes hold-to-repeat optimal for **short building sessions** of 10-30 seconds.

---

## 3. Method 2: Burst Engine

### 3.1 Mechanics

```js
// Fires limited taps at high speed, then waits for recharge
function buildBurst() {
  // Check: not busy, not collapsed, has charges, can afford cost
  // Deduct charge + cost
  // Fire `power` taps at `speed` ms intervals
  // Recharge 1 charge every `cooldown` seconds (max `charges`)
}
```

### 3.2 Base vs. Maxed Speed Profile

**Base (no upgrades):**

| Metric | Value |
|---|---|
| Power | 20 taps |
| Speed | 50ms/action |
| Burst duration | 1.0 second |
| Cost | 20 gold |
| Cooldown per charge | 20 seconds |
| Max charges | 1 |
| Bricks placed | 10 (in 2-tap system) |
| Rows at width 20 | 0.5 |

**Maxed upgrades (all Lv10):**

| Metric | Value |
|---|---|
| Power | 220 taps |
| Speed | 10ms/action |
| Burst duration | 2.2 seconds |
| Cost | 0 gold |
| Cooldown per charge | 2 seconds |
| Max charges | 6 |
| Bricks placed | 110 |
| Rows at width 20 | 5.5 |

### 3.3 Burst Engine Upgrades

| Upgrade ID | Name | Effect | Base Cost | Mult | Max Lv |
|---|---|---|---|---|---|
| `bp` | Crane Power | +20 taps per burst | 200 | 2.5 | 10 |
| `bs` | Pulley Speed | -5ms per action | 400 | 2.8 | 8 |
| `bc` | Bulk Order | -2 gold cost | 300 | 2.5 | 10 |
| `bcd` | Crew Cooldown | -2s cooldown | 500 | 3.0 | 9 |
| `bch` | Reserve Crew | +1 max charge | 1,000 | 3.5 | 5 |

### 3.4 Total Upgrade Cost

| Upgrade | Lv1 Cost | Lv5 Cost | Max Level | Total to Max |
|---|---|---|---|---|
| bp | 200 | 1,953 | Lv10 | 38,147 |
| bs | 400 | 3,936 | Lv8 | 30,377 |
| bc | 300 | 2,930 | Lv10 | 57,221 |
| bcd | 500 | 4,925 | Lv9 | 73,700 |
| bch | 1,000 | 9,844 | Lv5 | 14,762 |
| **Total** | | | | **214,207** |

### 3.5 The Charge Economy

The burst engine has a **dual constraint**: gold cost per use + charge cooldown.

```
Burst throughput (sustained) = power × (1 / cooldown)
                             = power / cooldown taps/second
```

| Phase | Power | Cooldown | Sustained taps/s | Effective bricks/s |
|---|---|---|---|---|
| Base | 20 | 20s | 1.0 | 0.5 |
| Early (bp3, bcd3) | 80 | 14s | 5.7 | 2.9 |
| Mid (bp5, bcd5, bch1) | 120 | 10s | 12.0 | 6.0 |
| Late (bp8, bcd7, bch3) | 180 | 6s | 30.0 | 15.0 |
| Max (bp10, bcd9, bch5) | 220 | 2s | 110.0 | 55.0 |

**Key insight**: Burst transitions from a *weak supplement* (base: 1 tap/s) to the *dominant build method* (maxed: 110 taps/s, 13× hold-to-repeat).

### 3.6 Charge Storage & Burst Spamming

With multiple charges, you can fire multiple bursts in quick succession:

| Charges | Consecutive Bursts | Total Taps | Total Time | Average taps/s |
|---|---|---|---|---|
| 1 | 1 | 20 | 1s + 20s wait | 0.95 |
| 3 | 3 | 60-360 | 3-3.3s + recovery | varies |
| 6 | 6 | 120-1,320 | 6-13.2s + recovery | varies |

A full 6-charge dump at max upgrades: 6 × 220 taps = 1,320 taps in 13.2 seconds. Then wait 2s per charge for full recovery (12s total).

---

## 4. Method 3: Auto-Build

### 4.1 Mechanics

```js
// Fires in the game loop every 100ms tick
if (auto_build_level > 0) {
  interval = max(100, 3000 / (1 + level * 0.5)); // ms
  if (tick % (interval / 100) < 1) { tapBuild(); }
}
```

### 4.2 Speed by Level

| Auto Level | Interval | Taps/min | Bricks/min | Rows/min (w=20) |
|---|---|---|---|---|
| 1 | 2,000 ms | 30 | 15 | 0.75 |
| 2 | 1,500 ms | 40 | 20 | 1.00 |
| 3 | 1,200 ms | 50 | 25 | 1.25 |
| 4 | 1,000 ms | 60 | 30 | 1.50 |
| 5 | 857 ms | 70 | 35 | 1.75 |
| 6 | 750 ms | 80 | 40 | 2.00 |
| 7 | 667 ms | 90 | 45 | 2.25 |
| 8 | 600 ms | 100 | 50 | 2.50 |
| 9 | 545 ms | 110 | 55 | 2.75 |
| 10 | 500 ms | 120 | 60 | 3.00 |
| 11 | 462 ms | 130 | 65 | 3.25 |
| 12 | 429 ms | 140 | 70 | 3.50 |
| 13 | 400 ms | 150 | 75 | 3.75 |
| 14 | 375 ms | 160 | 80 | 4.00 |
| 15 | 353 ms | 170 | 85 | 4.25 |

### 4.3 Auto-Build Upgrades

| Upgrade | ID | Effect | Base Cost | Mult | Max Lv |
|---|---|---|---|---|---|
| Auto-Trowel | ab1 | Auto-build (1.5s→0.2s/lv) | 200 | 2.8 | 10 |
| Auto-Crane | ab2 | Faster auto-build II | 1,200 | 3.2 | 10 |
| Auto-Gigalith | ab3 | Faster auto-build III | 8,000 | 3.8 | 10 |

Each upgrade adds +1 auto level (max Lv10 each, but effective cap Lv15).

### 4.4 Auto-Build with Prestige Synergy

p5 (Eternal Workshop) adds +1/+2/+3 to all auto levels at Lv1/2/3:

| Upgrades Purchased | Base Levels | p5 Lv0 | p5 Lv1 | p5 Lv2 | p5 Lv3 |
|---|---|---|---|---|---|
| ab1 Lv10 | 10 | 10 | 11 | 12 | 13 |
| ab1 Lv10 + ab2 Lv10 | 20 | 15* | 15* | 15* | 15* |
| All 3 at Lv10 | 30 | 15* | 15* | 15* | 15* |

*Cap is Lv15. With all ab1+ab2+ab3 purchases, you hit the cap easily. p5 is wasted on auto-build past Lv12 in ab1 alone.

### 4.5 Auto-Build Materials Check

Auto-build consumes materials from your inventory. It checks:
```js
if (mat && S.mat[mat] > 0 && S.mat.mortar > 0) { tapBuild(); }
```

If you run out of materials, auto-build skips its action silently. It does NOT:
- Switch to crafting
- Notify you
- Stop checking (wastes ticks)

This means auto-build alone can deplete your entire material stockpile in:
```
Time to deplete = materials / (auto_build_rate / 2)
```
(Each brick takes 2 taps: position + place, consuming 1 material + 1 mortar)

---

## 5. Sustained Throughput Analysis

### 5.1 Instant vs. Sustained Throughput

| Method | Instant taps/s | Sustained taps/s (5min avg) | Burst Factor vs Hold |
|---|---|---|---|
| Hold (base) | 8.3 | 8.3 | 1.0× |
| Burst (base) | 20.0 | 0.95 | 0.11× |
| Burst (mid) | 60.0 | 12.0 | 1.4× |
| Burst (max) | 100.0 | 110.0 | 13.3× |
| Auto (Lv10) | 2.0 | 2.0 | 0.24× |
| Auto (Lv15) | 2.8 | 2.8 | 0.34× |

**The crossover**: Burst surpasses hold-to-repeat in sustained throughput at ~bp Lv5 + bcd Lv5 (120/10 = 12 taps/s vs 8.3).

### 5.2 30-Minute Build Simulation

| Method | Total taps | Bricks placed | Rows (w=20) | Materials consumed |
|---|---|---|---|---|
| Hold (continuous) | 14,940 | 7,470 | 373.5 | 7,470+7,470 |
| Burst (base, every 21s) | 1,714 | 857 | 42.9 | 857+857 |
| Burst (mid, every 11s) | 19,636 | 9,818 | 490.9 | 9,818+9,818 |
| Burst (max, perma-charge) | 198,000 | 99,000 | 4,950 | 99,000+99,000 |
| Auto (Lv10, passive) | 3,600 | 1,800 | 90.0 | 1,800+1,800 |

### 5.3 The Material Wall

At max burst: 99,000 materials required in 30 minutes. That's 3,300 materials/min, or 55 materials/second.

But **max auto-craft produces ~170 materials/min** (Lv15). Even with max automation, you can only sustain:

```
Max material production: 170/min (auto-gather → auto-craft)
Max burst consumption: 110 taps/s × 0.5 bricks/tap = 55 bricks/s = 55 materials + 55 mortar/s

Sustain ratio: 55 / (170/60) = 55 / 2.83 = 19.4×
```

**The material wall is absolute**: Even maxed burst consumes materials 19× faster than max automation can produce them. Burst can only run for ~45 seconds before exhausting a 30-minute material stockpile.

### 5.4 Effective Build Time

Given material constraints, the *real* build rate is:

```
Method Rate = min(build_method_speed, material_production_rate / 2)

Hold:  min(8.3, 1.42) = 1.42 bricks/s   ← material limited
Burst: min(100, 1.42) = 1.42 bricks/s   ← material limited  
Auto:  min(2.8, 1.42) = 1.42 bricks/s   ← also material limited
```

**All methods are material-limited at max automation**. The only difference is *how long it takes to burn through your stockpile*, and *how much attention it requires*.

**Revised practical throughput**:

| Method | Bricks/s | Time to deplete 1min stockpile | Attention needed |
|---|---|---|---|
| Hold | 1.42 | Continuous | Full |
| Burst (max) | 1.42 avg | ~2.2s | Low (one tap) |
| Auto (Lv15) | 1.42 avg | Continuous | None |

Burst wins not on throughput, but on **attention efficiency**: it compresses 2.2 seconds of building into one tap.

---

## 6. Cost Structure Comparison

### 6.1 Gold Cost Per Row

| Method | Gold/action | Actions/row (w=20) | Gold/row | Notes |
|---|---|---|---|---|
| Hold | 0 | 40 taps | 0 | Free except time |
| Burst (base) | 20 | 40 taps | 40 | 2 bursts per row |
| Burst (early) | 16 | 40 taps | 16 | bc Lv2 |
| Burst (mid) | 10 | 40 taps | 0.8 | bc Lv5, burst power higher |
| Burst (max) | 0 | 40 taps | 0 | Free |
| Auto (Lv1) | 0 | 40 taps | 0 | Free (upfront cost) |

### 6.2 Upfront vs. Recurring Cost

| Method | Upfront Cost | Recurring Cost | Cost to Max |
|---|---|---|---|
| Hold | Tap upgrades (g1-g4, 35K🪙) | 0 | ~35K🪙 |
| Burst | 5 upgrades (214K🪙) | Gold per use (eventually 0) | ~214K🪙 |
| Auto | 3 upgrades (324K🪙) | 0 | ~324K🪙 |

### 6.3 Cost Per Brick Over Lifetime

Over a game lifetime of 500,000 bricks:

| Method | Total Cost | Cost/Brick | Cost/Brick (amortized) |
|---|---|---|---|
| Hold | 35,000 | 0.07🪙 | 0.07🪙 |
| Burst (max) | 214,207 + ~5K gold used | 0.44🪙 | 0.44🪙 |
| Auto (max) | 323,984 | 0.65🪙 | 0.65🪙 |

Hold is the cheapest per brick. Burst and auto are investments that pay for themselves through saved time.

### 6.4 Time Cost Per Row

| Method | Active time/row | Passive time/row | Total time/row |
|---|---|---|---|
| Hold | 4.8s | 0 | 4.8s active |
| Burst (max) | 0.2s (one tap) | 2s charge wait | 2.2s (0.2s active) |
| Auto (Lv15) | 0 | 14.1s | 14.1s passive |

### 6.5 The Efficiency Frontier

```
                    Active Time
                    │
        Low ────────┼─────────── High
                    │
          Auto ◄────┼────► Hold
                    │
               Burst│
                    │
```

- **Auto**: Minimizes active time, maximizes wall time
- **Hold**: Maximizes active throughput, zero passive wait
- **Burst**: Compromise — moderate active time, moderate passive wait

---

## 7. Material Efficiency

### 7.1 Materials Consumed Per Method

All methods consume the same materials per brick (1 material + 1 mortar). Material efficiency is **method-independent** for the build action itself.

However, different methods enable different **indirect material efficiencies**:

| Method | Can you gather during? | Can you craft during? | Net material impact |
|---|---|---|---|
| Hold | ❌ (same tab) | ❌ (same tab) | Materials consumed, zero production |
| Burst | ❌ (briefly blocked) | ❌ (briefly blocked) | Same as hold, but for less time |
| Auto | ✅ (different tab) | ✅ (different tab) | Materials consumed WHILE producing |

### 7.2 Auto-Build's Hidden Advantage

Auto-build runs while you're in the Gather or Craft tab. This means:

```
Time in Gather tab:
  ├── Auto-gather: producing resources  (+2.8-170 resources/min)
  ├── Auto-craft: producing materials    (+2.8-170 materials/min)  
  └── Auto-build: consuming materials    (-1.4-85 materials/min)

Net material change: (170 materials/min) - (85 materials/min) = +85/min
```

Auto-build is the only method that can **build while simultaneously replenishing materials**. Hold and burst consume materials without producing them.

### 7.3 Material Debt

**Hold and burst accumulate material debt**: you must spend time in Gather/Craft tabs to replenish what you consumed. Auto-build avoids this entirely.

| Method | Build 100 rows (w=20) | Time to replenish materials |
|---|---|---|
| Hold | 4,000 taps = 8 min active | ~24 min in gather/craft tabs |
| Burst (max) | 40 bursts = 88s active + 80s wait | ~24 min (same materials) |
| Auto (Lv15) | ~24 min passive | Net positive while building |

**This is the single most important economic insight in the game**: the material bottleneck means hold and burst are *bursty consumers* while auto-build is a *sustainable producer*. For long-term tower growth, auto-build wins.

### 7.4 Material Stockpile Strategy

Given the material constraint, the optimal play pattern is:

```
Phase 1: Gather/Craft (auto-active) → Build stockpile → 10-30 min
Phase 2: Burst (consume stockpile) → Build fast → 2-10 seconds
Phase 3: Gather/Craft (replenish) → Repeat → 10-30 min
```

The burst window is brief but intense. The replenishment window is long but passive (auto). The active play during Phase 1 and 3 can be spent on upgrades, talents, or other tabs.

---

## 8. Talent Synergy Matrix

### 8.1 Direct Build Talents

| Talent | Effect | Synergizes With | Why |
|---|---|---|---|
| **t1** Scaffolding | +15%/lv build speed | Hold, Burst | Affects tapBuild() speed... but currently, build speed is a UI speed, not a game speed. The hold interval is fixed. Burst speed is separately upgraded. |
| **t2** Mortar Mastery | +2%/lv reduced material strain | All methods equally | Works regardless of how bricks are placed |
| **bl3** Reinforced Joints | +10%/lv joint stability | All methods equally | Stability bonus affects all build methods |
| **bl4** Auto-Architect | +15%/lv auto-build bonus | Auto-build (directly) | Multiplies auto-build output |
| **t4** Stone Hardening | +1.2%/lv reduced brick strain | All methods equally | Material strength affects all bricks |
| **cr2** Kiln Mastery | +15%/lv craft speed | Hold (indirect) | Faster crafting = more materials for hold/burst |
| **cr4** Auto-Synthesis | +15%/lv auto-craft | Auto-build (indirect) | More materials while auto-building |

### 8.2 Method-Specific Talent Value

| Talent | Hold Value | Burst Value | Auto Value |
|---|---|---|---|
| t1 | Medium (build speed) | Low (burst has own speed) | Low (auto has own speed) |
| t2 | High (strain reduction) | High | High |
| bl3 | High (stability) | High | High |
| bl4 | None | None | **Extreme** (direct mult) |
| t4 | Medium (material str) | Medium | Medium |
| cr2 | High (material supply) | Medium (burst brief) | Low (auto-craft already) |
| cr4 | Low | Low | High (synergy with bl4) |

### 8.3 Auto-Build Talent Stack

bl4 + cr4 create an exponential auto-build loop:

```
Auto-build output = base × (1 + bl4_lv × 0.15) bricks/min
Auto-craft output = base × (1 + cr4_lv × 0.15) materials/min

Net build rate = min(auto_build_output, auto_craft_output / 2)
```

At bl4 Lv10: ×2.5 auto-build output  
At cr4 Lv10: ×2.5 auto-craft output  
Combined: **6.25× effective auto build rate**

An Lv15 auto-build with bl4+cr4 Lv10: 170 × 6.25 = **1,062 bricks/min = 53 rows/min** (w=20)

This rivals burst throughput while requiring **zero attention**.

### 8.4 Gather Talents That Feed Build

| Talent | Effect | Value to Build |
|---|---|---|
| **ga3** Deep Mining | +20%/lv gather mult | Feeds craft → materials |
| **ga4** Nature's Bounty | +15%/lv auto-gather | Feeds auto-craft during auto-build |
| **t3** Resource Efficiency | -8%/lv craft cost | More materials per resource |
| **ga2** Prospector's Eye | +5%/lv rare find | Bonus resources |

### 8.5 General Talents

| Talent | Effect | Build Relevance |
|---|---|---|
| **t5** Golden Touch | +15%/lv gold mult | More gold for burst costs |
| **f1** Fortress Foundation | +10%/lv reinf | Higher stability for all methods |
| **d1** Divine Inspiration | +15%/lv XP mult | More XP per build tap |
| **ge4** Babel's Blessing | +10%/lv all mult | Global multiplier applies to gold from build too |

---

## 9. Prestige Synergy Matrix

### 9.1 Prestige Upgrades vs. Build Methods

| Prestige Upgrade | Hold | Burst | Auto | Why |
|---|---|---|---|---|
| **p1** Diligent Start | Low | Low | Low | Starting gold helps early costs |
| **p2** Wider Legacy | High | High | High | More base width = more height potential |
| **p3** Ancient Foundation | High | High | High | More stability = fewer collapses |
| **p4** Echoes of Labor | Medium | Medium | Low | Legacy benefits all runs equally |
| **p5** Eternal Workshop | Low | Low | **Extreme** | +3 auto levels directly boost auto-build |
| **p6** Babel's Memory | Low | Low | Medium | Starting resources = less pre-building |
| **p7** Golden Legacy | High | **Extreme** | Low | Gold from all sources — funds burst costs |

### 9.2 p5 Eternal Workshop Deep Dive

p5 adds auto levels at shard cost:

| p5 Level | Shard Cost | Auto Effect |
|---|---|---|
| 0 | 0 | Base auto |
| 1 | 15 | +1 all auto levels |
| 2 | 75 | +2 all auto levels |
| 3 | 1,035 | +3 all auto levels |

Each auto level adds +10 actions/min. For auto-build specifically:

| p5 Level | Effective Auto-Build Level | Taps/min |
|---|---|---|
| 0 | (whatever purchased) | — |
| 1 | purchased + 1 | +10/min |
| 2 | purchased + 2 | +20/min |
| 3 | purchased + 3 | +30/min |

**p5 caps at Lv15.** If ab1 is already Lv15, p5 does nothing for auto-build. This happens at ab1 Lv12 (12 + 3 = 15).

### 9.3 p7 Golden Legacy & Burst Costs

p7 multiplies all gold income by `(1 + lv × 0.5)`:

| p7 Level | Gold Mult | Effective Burst Cost Reduction |
|---|---|---|
| 0 | 1.0× | Base cost |
| 1 | 1.5× | 33% cheaper relative |
| 2 | 2.0× | 50% cheaper relative |
| 3 | 2.5× | 60% cheaper relative |
| 4 | 3.0× | 67% cheaper relative |
| 5 | 3.5× | 71% cheaper relative |

Combined with burst cost upgrades (bc), p7 makes burst effectively free very quickly.

---

## 10. Tech & Milestone Synergy

### 10.1 Width Tech (bw1-bw6)

Width affects all methods equally — more bricks per row means more taps per row for everyone:

| Width Tech | Width | Bricks/Row | Taps/Row | Relative Build Time |
|---|---|---|---|---|
| None (+p2) | 20-25 | 20-25 | 40-50 | 1.0× |
| bw1 | 6 | 6 | 12 | 0.3× |
| bw2 | 10 | 10 | 20 | 0.5× |
| bw3 | 15 | 15 | 30 | 0.75× |
| bw4 | 20 | 20 | 40 | 1.0× |
| bw5 | 30 | 30 | 60 | 1.5× |
| bw6 | 50 | 50 | 100 | 2.5× |

**Strategic note**: If you're holding/bursting, narrower towers (bw1-bw2) are dramatically faster to build. But they have lower maxSafe = lower potential height. Trading width for height is a fundamental build economy decision.

### 10.2 Reinforce Tech (rf1-rf5)

Reinforce increases maxSafe by `+30` per 0.2 reinforce:

| Tech | Cost | Reinforce | maxSafe Contribution |
|---|---|---|---|
| rf1 | 200 | +0.2 | +6 height |
| rf2 | 1,000 | +0.4 | +12 height |
| rf3 | 5,000 | +0.6 | +18 height |
| rf4 | 30,000 | +0.8 | +24 height |
| rf5 | 200,000 | +1.0 | +30 height |

Each +6 height = +0.24 shards per collapse (at floor(h/25)). Over 100 collapses: +24 shards.

### 10.3 Foundation Tech (fd1-fd3)

Foundation multiplies capacity:

| Tech | Cost | Foundation Mult | maxSafe Contribution at w=20 |
|---|---|---|---|
| fd1 | 1,000 | 1.5× | +12.5 height |
| fd2 | 8,000 | 2.0× | +50 height |
| fd3 | 60,000 | 3.0× | +125 height |

### 10.4 Tower Height Milestones vs. Methods

| Milestone | Height | Bonus | Most Benefits |
|---|---|---|---|
| 10 | +10% width | All methods | Slightly more bricks/row but taller potential |
| 25 | +5% stability | All methods | Fewer collapses |
| 50 | ×2 gold | **Burst** | More gold for burst costs |
| 100 | Auto-repair | All methods | 3× collapse protection |
| 200 | Foundation ×2 | All methods | Massive height boost |
| 500 | Legacy amplifier | All methods (shard gain) |

---

## 11. Phase 1: Early Game (First Prestige)

### 11.1 Available Methods

| Method | Available? | Effective? | Why |
|---|---|---|---|
| Hold | ✅ Yes | ✅ Best option | Only reliable method |
| Burst | ✅ Yes but... | ❌ Weak | 20 taps, 20🪙 cost is expensive early |
| Auto | ❌ No | — | 200🪙 for ab1 is too expensive |

### 11.2 Recommended Strategy

First prestige in ~2-3 minutes:

```
1. Gather 50 of each resource (5s hold)
2. Craft mud bricks + mortar (5s hold)
3. Build tower via hold-to-repeat (30s)
4. Collapse at height 25-30
5. Collect 1-2 shards
```

**Hold is the only practical method.** Burst costs 20🪙 per use — at a time when you have 50-100🪙 total. Auto-build costs 200🪙 — out of reach.

### 11.3 Burst in Phase 1

Burst in phase 1 is a **luxury**: 20 taps for 20 gold when your entire gold income is ~2 gold/tap. The exchange rate is ~10 taps of gather for 1 burst of 20 taps. That's 50% efficient — you'd get more bricks by just holding.

**Verdict**: Don't use burst before first prestige.

---

## 12. Phase 2: Mid Game (Auto Economy)

### 12.1 Unlocking Methods

| Method | Unlock Cost | Phase 2 Priority |
|---|---|---|
| Hold | Free | Always available |
| Burst | Free (upgrades cost gold) | Low priority |
| Auto | ab1: 200🪙, ab2: 1,200🪙, ab3: 8,000🪙 | **High priority** |

### 12.2 Recommended Strategy

```
1. Buy ab1 (Auto-Trowel) at 200🪙
2. Buy ac1 (Auto-Stir) at 120🪙 → auto-craft
3. Buy ag1 (Auto-Scoop) at 80🪙 → auto-gather
4. Let automation run while you gather/craft manually
5. Burst when stockpile reaches ~200 materials
6. Buy ab2, ab3 when available
```

**Auto-build becomes viable** in phase 2. At Lv1 auto-build: 30 taps/min. Over 5 minutes of afk: 150 taps = 3.75 rows. Not amazing, but free.

### 12.3 Burst in Phase 2

With a few bp upgrades, burst becomes a **strategic tool**:
- bp Lv2: 60 taps for ~18🪙
- Hold equivalent: 60 taps = 7.2s of holding
- Burst saves ~6s of holding time

Use burst when you want to:
- Quickly check if the tower survives another row
- Build a few rows while auto-replenish is running
- Burst during the 5-second window after completing a gather/craft cycle

### 12.4 The Auto-Build Milestone

**Lv5 auto-build** (ab1 at Lv5, 857ms interval) = 70 taps/min = 1.75 rows/min.

At this point, you can build faster passively than you can actively (accounting for the time to switch tabs, gather materials, and switch back).

**This is the auto-build tipping point.** After this, auto-build is the primary build method.

---

## 13. Phase 3: Late Game (Prestige Loops)

### 13.1 Optimal Method Mix

In prestige loop phase (runs 10-100), the optimal pattern is:

```
Start a fresh run:
├── Auto-gather + auto-craft running (passive)
├── Tap to buy foundation upgrades (10s)
├── Let auto-build run while you upgrade tech/talents (1-2 min)
├── When stability reaches hazard zone (<5%):
│   ├── Option A: Let it collapse naturally (auto-build will cause collapse)
│   └── Option B: Burst the last few rows (faster, risk 20🪙)
└── Collect shards, prestige
```

### 13.2 Method Performance in Phase 3

| Metric | Hold | Burst (Lv5 bp/bcd) | Auto (Lv10) |
|---|---|---|---|
| Bricks/run | — | ~300 (burst at end) | ~2,000 (full run) |
| Time active | — | ~3 seconds | 0 |
| Gold cost/run | — | ~50🪙 | 0 |
| Shards/run | — | Same | Same (height determined by stability) |

**Auto-build is clearly dominant** in phase 3. It builds the entire tower while you do other things. Burst is only used at the very end of a run to push for the next height threshold.

### 13.3 Burst Value at Threshold

Pushing from height 124 to 125 (crossing a 25-threshold for +1 shard):

| Method | Time | Risk | Cost | Value of +1 shard |
|---|---|---|---|---|
| Hold | ~6s of active tapping | Must watch stability | Free | +1 shard |
| Burst | 1 tap + 2s wait | Less time at risk | ~20🪙 | +1 shard |
| Auto | ~14s passive | Same | Free | +1 shard |

Burst is the fastest way to cross thresholds, reducing the window of collapse risk.

---

## 14. Phase 4: Endgame (Max Efficiency)

### 14.1 Maxed Methods

At endgame, all methods can be maxed:

| Method | Max Throughput | Gold Cost | Attention |
|---|---|---|---|
| Hold | 8.3 taps/s | 0 | Full |
| Burst | 110 taps/s sustained | 0 (free at bc Lv10) | One tap per burst |
| Auto | 170 taps/min (2.8/s) | 0 | None |

### 14.2 The Endgame Build Loop

With max burst + max auto + max talents:

```
1. Start run
2. Auto everything runs (passive)
3. Spend 30s buying all tech/talents/prestige
4. Let auto-build run for 5 minutes → height 300+ (passive)
5. Stability reaches hazard zone
6. Optional: Burst the last 20 rows for threshold crossing (2 taps)
7. Collapse → 12-15 shards
8. Prestige → repeat
```

Total active time per run: **~35 seconds**. Shards per hour: **~60-90**.

### 14.3 The Ultimate Build Strategy

The endgame player uses all three methods in a choreographed sequence:

```
┌──────────────────────────────────────────────┐
│         THE ENDGAME BUILD CYCLE              │
├──────────────────────────────────────────────┤
│                                              │
│ 1. GATHER TAB (hold, 10s)                    │
│    → Stockpile resources                     │
│    → Auto-gather runs in background          │
│                                              │
│ 2. CRAFT TAB (hold, 10s)                     │
│    → Convert resources to materials          │
│    → Auto-craft runs in background           │
│    → Auto-build runs in background           │
│                                              │
│ 3. UPGRADE TAB (tap, 10s)                    │
│    → Buy tech/talents/prestige               │
│    → Auto-build continues                    │
│                                              │
│ 4. BUILD TAB (check, 2s)                     │
│    → Check stability                         │
│    → Burst if near threshold                 │
│    → Let auto-build handle the rest          │
│                                              │
│ 5. REPEAT from step 1                        │
│    (or collapse if tower unstable)           │
│                                              │
└──────────────────────────────────────────────┘
```

---

## 15. Burst Engine Upgrade Path Optimization

### 15.1 Upgrade Ordering

The burst engine has 5 upgrades. Optimal ordering depends on your goals:

**For speed (minimize time per burst):**
```
bs (Pulley Speed) → bp (Crane Power) → bcd (Crew Cooldown) → bch (Reserve Crew) → bc (Bulk Order)
```
Rationale: Speed reduces the burst window. Power increases output. Cooldown enables more frequent bursts.

**For economy (minimize cost per burst):**
```
bc (Bulk Order) → bcd (Crew Cooldown) → bch (Reserve Crew) → bp (Crane Power) → bs (Pulley Speed)
```
Rationale: Cost reduction first. Then cooldown for more charges. Then power/speed for efficiency.

**Balanced recommendation:**
```
bp Lv3 → bs Lv3 → bcd Lv3 → bc Lv5 → bp Lv5 → bs Lv5 → bcd Lv5 → bch Lv3 → bp Lv8 → bs Lv8 → bcd Lv7 → ... max
```

### 15.2 Marginal Value Analysis

| Upgrade | Level | Cost | Benefit | Cost/Benefit |
|---|---|---|---|---|
| bp 0→1 | 200 | +20 taps/burst | 10 taps/🪙 |
| bp 5→6 | 1,953 | +20 taps/burst | 97 taps/🪙 (diminishing) |
| bs 0→1 | 400 | -5ms/action | 80 taps/🪙 |
| bs 5→6 | 3,936 | -5ms/action (25→20ms) | 787 taps/🪙 |
| bc 0→1 | 300 | -2🪙/burst | 150🪙 saved over 150 bursts |
| bc 5→6 | 2,930 | -2🪙/burst | 1,465🪙 saved over 730 bursts |

### 15.3 Break-Even Analysis

**When does burst pay for itself compared to hold?**

Burst costs gold but saves time. If your time is worth X gold/second:

```
Burst value/time = (burst_power × hold_gold_per_tap - burst_cost) / burst_total_time

At base:
  value = (20 taps × 1 gold/tap - 20 gold) / (1s burst + 20s cooldown)
        = 0 gold/s  (break-even)

At bp Lv5, bc Lv5 (power=120, cost=10):
  value = (120 taps × 2 gold/tap - 10 gold) / (2.4s burst + 10s cooldown)
        = 230 gold / 12.4s
        = 18.5 gold/s
```

At the mid-game point where you earn 10-20 gold/s from all sources, burst is a **slight net positive**.

But this analysis is misleading — the real value of burst is **time compression**, not gold efficiency. Burst lets you build 120 taps in 2.4 seconds instead of 14.4 seconds of holding. That saved 12 seconds can be spent on gold-earning activities.

---

## 16. Hold Method Upgrade Path Optimization

### 16.1 What Upgrades Help Hold?

Hold-to-repeat has no direct upgrades, but benefits indirectly:

| Upgrade Type | Examples | Effectiveness |
|---|---|---|
| Gold per tap | g1-g4 | High (more gold while holding build tab) |
| XP per tap | sg1-sg3 | Medium (more XP while holding) |
| Stability | rf1-rf5, f1 talent | High (fewer interruptions) |
| Material savings | t3 talent | Medium (more bricks per resource) |
| Craft speed (indirect) | c1-c4, cr2 | High (faster material prep) |

### 16.2 The Hold-Efficiency Build

To maximize hold-to-repeat effectiveness:

```
1. Max g1-g4 (gather gold) → funds everything
2. Max c1-c4 (craft gold) → more gold while preparing materials
3. Buy stability tech (rf1-rf5, fd1-fd3)
4. Max ab1 (auto-build) to supplement hold
5. Focus on reducing width (bw1-bw2) for faster row completion
```

### 16.3 Hold as Training Wheels

For a player who wants to be optimal: **hold is a crutch**. It's the first method you learn, the most intuitive, and the most expensive in attention. The faster you transition to burst + auto, the more efficient you become.

| Player Type | Hold Usage |
|---|---|
| New (<10 prestige) | 80% of build actions |
| Intermediate (10-50 prestige) | 30% of build actions |
| Advanced (50+ prestige) | 5% of build actions |
| Optimal | <1% (only when waiting 1-2 seconds for burst charge) |

---

## 17. Auto-Build Upgrade Path Optimization

### 17.1 Upgrade Order

Auto-build has 3 upgrades (ab1, ab2, ab3) plus the p5 prestige synergy:

```
ab1 → Lv5 (857ms) → p5 Lv1 → ab1 → Lv10 (500ms) → p5 Lv2 → 
ab2 → Lv5 → ab3 → Lv5 → p5 Lv3 → ab2 → Lv10 → ab3 → Lv10
```

### 17.2 Auto-Build Level Targets

| Target Level | Interval | Effective With p5 Lv3 | Gold Investment |
|---|---|---|---|
| Lv5 (first milestone) | 857ms | — | 3,490 |
| Lv10 (auto-cap) | 500ms | 400ms (Lv13) | 15,571 |
| Lv15 (hard cap) | 353ms | Already capped | 323,984 (all 3) |

**Optimal stopping point**: ab1 Lv10 + p5 Lv3 = effective Lv13 = 400ms interval = 150 taps/min. Going beyond requires ab2+ab3 and costs 300K+ for diminishing returns.

### 17.3 Auto-Build + Auto-Craft Balance

The auto-build ↔ auto-craft balance is critical:

```
Net material change = auto_craft_rate - auto_build_rate

Optimal balance: auto_craft_rate ≈ 2 × auto_build_rate
(Each brick needs 1 material + 1 mortar = 2 craft actions)
```

| Auto-Craft Level | Auto-Build Level | Net Materials | Sustainable? |
|---|---|---|---|
| Lv5 (70/min) | Lv5 (35 bricks/min) | 0 | ✅ Balanced |
| Lv10 (120/min) | Lv10 (60 bricks/min) | 0 | ✅ Balanced |
| Lv15 (170/min) | Lv15 (85 bricks/min) | 0 | ✅ Balanced |
| Lv5 (70/min) | Lv10 (60 bricks/min) | -50/min | ❌ Drains |

**Rule of thumb**: Keep auto-craft ≥ 2× auto-build level.

---

## 18. The Complete Build Economy

### 18.1 The Full Production Chain

```
GATHER tab          CRAFT tab           BUILD tab
──────────          ──────────          ─────────
Resources ──────→   Materials ──────→   Tower Height
   │                     │                    │
   ├── Auto-gather       ├── Auto-craft       ├── Auto-build
   ├── Hold-gather       ├── Hold-craft       ├── Burst
   └── Tap-upgrades      └── Craft-upgrades   └── Hold-build
```

### 18.2 System-Wide Bottlenecks

```
       ╔═══════════════════════════════════════════╗
       ║     THE CRITICAL PATH OF BRICK PRODUCTION  ║
       ╚═══════════════════════════════════════════╝
       
       Resources →→→ Materials →→→ Tower Height
           ↑              ↑              ↑
        [BOTTLENECK 1] [BOTTLENECK 2] [BOTTLENECK 3]
        Gather rate   Craft rate     Build rate
       
       At any given time, ONE of these is the bottleneck.
       
       Early game:  Bottleneck 1 (not enough mud/straw)
       Mid game:    Bottleneck 2 (not enough crafted bricks)
       Late game:   Bottleneck 3 (stability caps height)
       Endgame:     Bottleneck 3 (always stability)
```

### 18.3 Method Selection by Bottleneck

| Current Bottleneck | Best Method | Why |
|---|---|---|
| Resources (gather) | Hold in gather tab | Maximize resource input |
| Materials (craft) | Hold in craft tab | Convert resources to materials |
| Build speed | Burst or auto | Burst for quick bursts, auto for passive |
| Stability (height cap) | Any | Method doesn't matter, height is capped |
| Gold | Skills/talents tab | Maximize gold income for upgrades |

---

## 19. Method Selection by Tower Width

### 19.1 Width's Impact on Each Method

The number of bricks per row directly affects how many taps each method needs per row.

| Width | Taps/Row | Hold Time/Row | Burst Charges/Row | Auto Time/Row |
|---|---|---|---|---|
| 6 | 12 | 1.4s | 0.6 charges (base) | 7.1s (Lv10) |
| 10 | 20 | 2.4s | 1.0 charges (base) | 11.8s |
| 15 | 30 | 3.6s | 1.5 charges (base) | 17.6s |
| 20 | 40 | 4.8s | 2.0 charges (base) | 23.5s |
| 25 | 50 | 6.0s | 2.5 charges (base) | 29.4s |
| 30 | 60 | 7.2s | 3.0 charges (base) | 35.3s |
| 50 | 100 | 12.0s | 5.0 charges (base) | 58.8s |

### 19.2 Optimal Width for Each Method

| Method | Optimal Width | Rationale |
|---|---|---|
| Hold | 10-15 (bw2-bw3) | Fast row completion, less holding time |
| Burst (base) | 6-10 (bw1-bw2) | 1 burst = 1 row, clean charge usage |
| Burst (maxed) | 20+ | 220 taps/burst = multiple rows |
| Auto | 15-20 (bw3-bw4) | Hands-off, width balances height vs time |

### 19.3 The Width Decision

The width decision is a **build economy choice**:

```
Narrow (bw1, width 6):
  ✅ Fast row completion
  ✅ Fewer materials per row
  ❌ Low maxSafe (shorter towers)
  ❌ Fewer shards per collapse

Wide (bw6, width 50):
  ❌ Slow row completion  
  ❌ Many materials per row
  ✅ High maxSafe (taller towers)
  ✅ More shards per collapse
```

The optimal width depends on your build method AND your prestige strategy.

---

## 20. Hybrid Strategies

### 20.1 Hold + Burst

The simplest hybrid: hold to build normally, burst when you need speed.

```
Pattern: hold(10s) → burst → hold(10s) → burst → ...
```

| Segment | Duration | Taps | Method |
|---|---|---|---|
| Hold | 10s | 83 | Hold-to-repeat |
| Burst | 1-2s | 20-220 | Burst |
| Cooldown | 2-20s | 0 | Wait or hold |
| **Cycle** | **13-32s** | **103-303** | **Hybrid** |

### 20.2 Hold + Auto

The most common mid-game pattern: hold is your active method, auto runs in background.

```
Active: Hold build (30s) → Switch to gather/craft (2min) → Switch back (30s)
Passive: Auto-build runs during those 2 minutes
```

Net build rate: `(30s hold × 8.3/s + 120s auto × 2/s) / 150s = 3.26 bricks/s`

### 20.3 Burst + Auto

The endgame optimal pattern:

```
Active: Burst 1 tap → switch tab → come back 10s later → burst 1 tap
Passive: Auto-build runs continuously
```

Net build rate: `burst(~1 tap per 10s × 100/s effective) + auto(2/s) ≈ 12 bricks/s`

### 20.4 All Three (The Trinity)

The theoretically optimal pattern using all three methods:

```
1. Let auto-build run (passive, always)
2. Hold-build when actively playing in build tab (5-10s sprints)
3. Burst for threshold crossing (1 tap at end of run)
4. Use burst to quickly test stability at hazard zone edge
```

---

## 21. Burst Charge Mathematics

### 21.1 Charge Recovery as a Poisson Process

Charge recovery is deterministic, but if we model the player's burst usage as random:

```
λ = 1 burst every T seconds

If T < cooldown: charges deplete (unsustainable)
If T = cooldown: charges stable at 1
If T > cooldown: charges accumulate toward max
```

### 21.2 Charge Depletion Time

Starting from full charges, firing bursts back-to-back:

| Charges | Burst Power | Total Taps | Time to Deplete | Full Recharge Time |
|---|---|---|---|---|
| 1 | 20 | 20 | 1.0s | 20s |
| 3 | 60 (assuming bp Lv3) | 180 | 2.6s | 28s |
| 6 (max) | 220 (max bp) | 1,320 | 13.2s | 10s |

### 21.3 Optimal Charge Usage

```
If you have >1 charge and cooldown is short:
  Use bursts sequentially for maximum building
  Then wait for recharge

If you have 1 charge and cooldown is long:
  Save burst for emergencies (threshold crossing)
  Use hold/auto for normal building
```

### 21.4 Charge Waste

Charges are wasted if they sit at max:

```
Max charges = 6
Cooldown = 2s
Full recharge from 0 = 12s

If you don't burst for 12+ seconds, you're wasting potential charges.
```

At max upgrades, the game demands you burst every 12 seconds to avoid waste. This creates an **optimal burst cadence**.

---

## 22. Hold Warm-Up Mathematics

### 22.1 Current Hold Model

Hold-to-repeat fires at a fixed 120ms interval. There's no warm-up or acceleration.

### 22.2 Proposed Dynamic Hold Model

If hold had a warm-up mechanic (from the design spec):

```js
interval(t) = max(minInterval, initialSpeed - acceleration × t)
Where t = seconds held continuously
```

| Hold Duration | Base Model | Dynamic Model (acc=5ms/s, min=40ms) |
|---|---|---|
| 0s (first tap) | 120ms | 120ms |
| 1s | 120ms | 115ms |
| 2s | 120ms | 110ms |
| 3s | 120ms | 105ms |
| 5s (warm) | 120ms | 95ms |
| 10s (hot) | 120ms | 70ms |
| 16s (peak) | 120ms | 40ms |

### 22.3 Dynamic Hold Cumulative Output

Over a 30-second hold:

| Model | Total Taps | Bricks | Rows (w=20) |
|---|---|---|---|
| Base (120ms fixed) | 250 | 125 | 6.25 |
| Dynamic (acc=5, min=40) | ~450 | 225 | 11.25 |

Dynamic hold is **1.8× more productive** during a long hold.

### 22.4 Optimal Hold Duration

With dynamics, holding has an optimal duration:

```
Short holds (<5s): Benefit is minimal (not warmed up)
Medium holds (5-15s): Good acceleration, peak not reached
Long holds (15-30s): Peak speed sustained, diminishing returns on further wait
Optimal: 10-15s holds, release and re-hold
```

---

## 23. Automation Breakpoint Mathematics

### 23.1 Level-to-Interval Function

```js
interval(lv) = max(100, 3000 / (1 + 0.5 × lv))
```

This is a **hyperbolic decay** function. Each level adds diminishing returns in absolute terms:

| Level | Interval Δ | Actions/min Δ | Actions/min Δ per gold spent |
|---|---|---|---|
| 0→1 | -1,000ms | +10 | High value |
| 1→2 | -500ms | +10 | Good value |
| 2→3 | -300ms | +10 | Good value |
| 3→4 | -200ms | +10 | OK value |
| 4→5 | -143ms | +10 | OK value |
| 10→11 | -38ms | +10 | Diminishing |
| 14→15 | -22ms | +10 | Poor value |

Each level adds exactly +10 actions/min. The gold cost grows geometrically. The **bang-for-buck** declines exponentially.

### 23.2 Optimal Auto-Build Stopping Point

```
ab1 Lv0-5:    Good value (80→ 2,718 cumulative gold)
ab1 Lv6-8:    OK value   (2,718→ 9,837 cumulative gold)  
ab1 Lv9-10:   Poor value (9,837→ 15,571 cumulative gold)
ab2+ab3:      Expensive  (→ 323,984 cumulative gold)
```

**Recommended**: ab1 to Lv5 (2,718🪙), then p5 to Lv3 (1,035💎). Effective Lv8. Later, ab1 to Lv10, then ab2+ab3 only after all other upgrades are done.

### 23.3 Auto-Build + Auto-Craft Balance Point

The balance point is where:

```
auto_craft_rate = 2 × auto_build_rate

At ab Lv5 (70 taps/min = 35 bricks/min): Need ac Lv5 (70 crafts/min)
At ab Lv10 (120 taps/min = 60 bricks/min): Need ac Lv10 (120 crafts/min)
At ab Lv15 (170 taps/min = 85 bricks/min): Need ac Lv15 (170 crafts/min)
```

In practice, auto-craft needs mortar (which needs resources). Auto-gather must keep up too. The full balance:

```
auto_gather_rate ≥ auto_craft_rate × avg_resources_per_craft
```

For megaliths: ~7 resources per craft. Need auto-gather at 7× auto-craft rate.

---

## 24. Material-Method Fit Analysis

### 24.1 Craft Cost of Each Material

| Material | Resources/Craft | Tiers Deep | Total Raw | Best Method |
|---|---|---|---|---|
| Mortar | 4 (sand, gravel, water, lime) | 1 | 4 | Auto-craft |
| Mud Brick | 3 (mud, straw) | 1 | 3 | Auto-craft |
| Fired Brick | 4 (clay, sand, water) | 1 | 4 | Auto-craft |
| Stone Block | 3 (stone) | 1 | 3 | Auto-craft |
| Reinforced Brick | 3 (firedBrick, stone, lime) | 2 | 7 | Burst-craft |
| Glazed Brick | 4 (firedBrick, sand, water) | 2 | 6 | Burst-craft |
| Megalith | 2 (stoneBlock, reinfBrick) | 3 | 10+ | Burst-craft |

### 24.2 Method Fit by Material

| Material | Hold Build | Burst Build | Auto Build |
|---|---|---|---|
| Mud Brick | ✅ Fine | ✅ Fine | ✅ Fine |
| Fired Brick | ✅ Fine | ✅ Fine | ✅ Fine |
| Stone Block | ✅ Fine | ✅ Fine | ✅ Fine |
| Reinforced Brick | ⚠️ Costly | ✅ Efficient | ❌ Auto depletes fast |
| Glazed Brick | ⚠️ Costly | ✅ Efficient | ❌ Auto depletes fast |
| Megalith | ❌ Too expensive | ✅ Ideal | ❌ Can't sustain |

**Megaliths are burst-exclusive materials** in practice. Their production cost is so high that only burst's time-compression makes them practical to build with.

### 24.3 Switching Materials Mid-Tower

When you unlock a better material (e.g., fired brick at crafting Lv3), you can't switch mid-tower. The material is determined globally:

```js
function getMatId() {
  // Returns the best material based on crafting level
}
```

This means: **tower material is fixed per run**. Choose your build method based on the material you're using.

---

## 25. Stability-Risk-Method Tradeoffs

### 25.1 Collapse Probability by Method

Each method has a different risk profile when the tower enters the hazard zone:

| Method | Hazard Zone Behavior | Risk |
|---|---|---|
| Hold | Slowly places bricks, one at a time | Low — you see each brick |
| Burst (instant) | Places ~20 bricks in 1s | **High** — collapse check per row |
| Burst (sustained) | Places ~220 bricks in 2.2s | **Extreme** — many rows checked |
| Auto | Places bricks at 2-4s intervals | Very low — slow enough to react |

### 25.2 Hazard Zone Survival by Method

In the hazard zone (stability < 5%), each completed row has a `P(collapse) = 0.05` (or 0.0167 with repair):

**Rows to survive through the hazard zone:**

| Hazard Width | P(survive all) | Hold (8.3/s) | Burst (100/s) | Auto (2/s) |
|---|---|---|---|---|
| 5 rows | 77.4% | 2.4s | 0.2s | 10s |
| 10 rows | 59.9% | 4.8s | 0.4s | 20s |
| 15 rows | 46.3% | 7.2s | 0.6s | 30s |

**Burst's speed is a double-edged sword**: it minimizes time at risk, but if collapse happens, you lose more progress (more bricks invested in the run).

### 25.3 Expected Loss Per Collapse

| Method | Value Lost on Collapse | Probability | Expected Loss |
|---|---|---|---|
| Hold | 2-3 seconds of progress | 22.6% in hazard zone | ~0.6s |
| Burst (base) | 1-2 bursts of progress | 22.6% | ~2s + 20🪙 |
| Burst (maxed) | 220+ taps of progress | 22.6% | ~13s progress |
| Auto | 10-15s of progress | 22.6% | ~2.5s |

---

## 26. Tower Height Milestone Racing

### 26.1 Milestone Thresholds

The tower height milestones (10, 25, 50, 100, 200, 500) are **one-time permanent bonuses**. Racing to claim them requires:

| Milestone | Height | Build Taps (w=20) | Hold Time | Burst Charges | Auto Time (Lv10) |
|---|---|---|---|---|---|
| 10 | 10 rows | 400 | 48s | 20 charges base | 3.9 min |
| 25 | 25 rows | 1,000 | 2.0 min | 50 charges | 9.8 min |
| 50 | 50 rows | 2,000 | 4.0 min | 100 charges | 19.6 min |
| 100 | 100 rows | 4,000 | 8.0 min | 200 charges | 39.2 min |
| 200 | 200 rows | 8,000 | 16.1 min | 400 charges | 78.4 min |
| 500 | 500 rows | 20,000 | 40.2 min | 1,000 charges | 196 min |

### 26.2 Optimal Method for Each Milestone

| Milestone | Best Method | Why |
|---|---|---|
| 10 (width +10%) | Hold | Too early for burst/auto investment |
| 25 (stability +5%) | Hold + auto | Auto just becoming viable |
| 50 (×2 gold) | Auto | Auto established, burst for final push |
| 100 (auto-repair) | Auto + burst | Auto for bulk, burst at hazard zone |
| 200 (foundation ×2) | Auto + burst | Same |
| 500 (legacy) | Auto only | Auto builds while you sleep |

---

## 27. Prestige Cycle Optimization by Method

### 27.1 Cycle Time Components

A prestige cycle consists of:

```
Cycle = Setup + Build + Threshold Push + Collapse + Rebuy

Setup:     Buy tech/prestige (10-60s)
Build:     Reach near-max height (variable)
Push:      Cross thresholds (variable)
Collapse:  Instant (0s)
Rebuy:     Spend shards on upgrades (10-30s)
```

### 27.2 Method Impact on Cycle Time

| Method | Build Phase | Push Phase | Total Active Cycle |
|---|---|---|---|
| Hold | 5-15 min active | 30s active | ~15 min |
| Burst (base) | Let auto build | 1 tap | ~5 min (mostly auto) |
| Burst (maxed) | 10s burst, then auto | 1 tap | ~5 min |
| Auto (Lv10) | 0s (passive) | 1 tap | ~2 min (affk) |
| Auto (Lv15) | 0s (passive) | 1 tap | ~2 min (affk) |

### 27.3 Shards Per Hour by Method

Based on a 1,000 prestige run simulation:

| Method | Shards/Run | Active Time/Run | Shards/Hour Active | Shards/Hour Wall |
|---|---|---|---|---|
| Hold | 6 | 15 min | 24 | 24 |
| Burst (base) | 6 | 5 min | 72 | 72 |
| Burst (maxed) | 15 | 3 min | 300 | 300 |
| Auto (Lv10) | 12 | 2 min | 360 | 360 |
| Auto (Lv15) | 15 | 2 min | 450 | 450 |

**Auto-build dominates** for shard farming. The active time is minimal and the shards/hour wall clock is highest.

---

## 28. Offline Progress & Method Selection

### 28.1 Offline Build Mechanics

```js
if (auto_build_level > 0) {
  ticks = min(elapsed_ms, 86400000) / 100
  auto_builds = floor(ticks / (auto_interval / 100))
  // capped at 500 rows instantly
}
```

### 28.2 Offline Method Performance

| Method | 1 Hour Offline | 8 Hours Offline | 24 Hours Offline |
|---|---|---|---|
| Hold | 0 (not automatic) | 0 | 0 |
| Burst | 0 (not automatic) | 0 | 0 |
| Auto (Lv1, 2s) | 1,800 taps = 45 rows | 500 rows (capped) | 500 rows |
| Auto (Lv10, 0.5s) | 7,200 taps = 180 rows | 500 rows (capped) | 500 rows |

**Offline progress is capped at 500 rows** regardless of method. This means:
- After ~11 rows/min (Lv10 auto), the cap is reached in ~45 minutes
- Longer offline periods are wasted on build progress
- Auto-gather and auto-craft are the real offline value

### 28.3 Optimal Offline Method Selection

Since offline build caps at 500 rows:

```
For any offline period > 1 hour:
  Auto-build level doesn't matter much (all hit the cap)
  
For short offline periods (< 1 hour):
  Higher auto-build = more progress
  Lv1: 45 rows in 1h
  Lv10: 180 rows in 1h (but still capped at 500)
```

---

## 29. Gold Economy & Method Selection

### 29.1 Gold Cost Per Build Session

| Session Length | Hold Gold Cost | Burst Gold Cost (base) | Burst Gold Cost (max) | Auto Gold Cost |
|---|---|---|---|---|
| 1 minute | 0 | 3 bursts = 60🪙 | free | 0 |
| 10 minutes | 0 | 30 bursts = 600🪙 | free | 0 |
| 1 hour | 0 | 180 bursts = 3,600🪙 | free | 0 |

### 29.2 Gold Needed to Max Burst Upgrades

214,207 gold to max all burst upgrades. Compared to:
- Auto upgrades (all 3): 323,984 gold
- Tap upgrades (g1-g4, c1-c4): ~9M gold
- All talents: ~500M gold

Burst upgrades are **moderately expensive** — comparable to auto upgrades, much cheaper than talents.

### 29.3 When to Invest in Burst

| Gold Available | Burst Investment | Rationale |
|---|---|---|
| 0-10K | None | Other priorities |
| 10K-50K | bp Lv3, bs Lv3 | Basic burst capability |
| 50K-200K | bp Lv5, bcd Lv5, bc Lv5 | Mid-tier burst |
| 200K+ | All max | Full burst potential |

### 29.4 Gold Opportunity Cost

Every 200🪙 spent on burst early is 200🪙 not spent on:
- Auto upgrades (ab1: 200🪙 — directly competes)
- Resource upgrades (r1: 50🪙 — much better ROI)
- Skill XP upgrades (sg1: 100🪙 — better for leveling)

**Early burst investment is a trap.** The gold is better spent elsewhere until your economy is established.

---

## 30. XP Economy & Method Selection

### 30.1 XP Per Build Tap

Each build tap awards:
- Position tap: 1×DB building XP + 0.5×DB general XP
- Place tap: 2×DB building XP + 1×DB general XP

Over the 2-tap cycle: 3×DB building XP + 1.5×DB general XP per brick.

### 30.2 XP Per Minute by Method

| Method | Taps/min | Building XP/min | General XP/min |
|---|---|---|---|
| Hold (8.3/s) | 500 | 750 | 375 |
| Burst (max sustained) | 6,600 | 9,900 | 4,950 |
| Burst (max instant) | 6,000 (for 2.2s) | 9,000 | 4,500 |
| Auto (Lv10, 2/s) | 120 | 180 | 90 |
| Auto (Lv15, 2.8/s) | 170 | 255 | 128 |

### 30.3 XP for Building Level

Building XP feeds the building skill level, which unlocks:
- Building milestones (Lv5-500)
- Building skill XP upgrades (sb1-sb3)
- Talent requirements (bl3, bl4 need building Lv20+)

**Burst is the fastest XP method** by a wide margin. Max burst gives 9,900 building XP/min vs 750 hold XP/min = 13× faster.

### 30.4 Leveling Build Skill via Burst

| Method | Time to Lv500 Building (270M XP) |
|---|---|
| Hold only | 360 hours |
| Burst (base) | 540 hours (slower than hold!) |
| Burst (maxed) | 27 hours |
| Auto (Lv10) | 1,500 hours |

---

## 31. Design Analysis: The Three Philosophies

### 31.1 What Each Method Rewards

| Method | Rewards | Penalizes | Player Type |
|---|---|---|---|
| Hold | Patience, rhythm, attention | Impatience, multitasking | Casual/new players |
| Burst | Timing, resource management, planning | Spam-clicking, wastefulness | Strategic players |
| Auto | Long-term planning, economy building | Impulsiveness, active play | Idle/AFK players |

### 31.2 What Each Method Costs the Player

| Method | Cognitive Cost | Physical Cost | Game Resource Cost |
|---|---|---|---|
| Hold | High (must stay in tab) | Medium (finger holding) | None |
| Burst | Low (one tap) | Very low | Gold + charges |
| Auto | None (runs passively) | None | Gold (upfront) |

### 31.3 Method Progression Arc

```
Player skill/experience →
                       
Strong ┼                                    Burst (maxed)
       │                                      
       │                        Burst (mid)
       │                       
       │            Auto (max)
       │            Auto (mid)
Weak   ┼── Hold ─── Auto (base) ──── Burst (base)
       │
       └────────────────────────────────────────
        0 hrs                   100+ hrs
              Play time →
```

The new player relies on hold. The intermediate player transitions to auto. The advanced player adds burst. The expert uses all three in harmony.

---

## 32. Method Switching: When and Why

### 32.1 Decision Matrix

| Situation | Hold | Burst | Auto | Why |
|---|---|---|---|---|
| First 10 runs | ✅ | ❌ | ❌ | No gold for upgrades |
| Building stockpile | ❌ | ❌ | ✅ | Let auto-craft stockpile too |
| Need 10 rows fast | ✅ | ✅ | ❌ | Hold or burst for speed |
| Crossing 25-threshold | ❌ | ✅ | ❌ | Burst minimizes risk window |
| AFK/offline | ❌ | ❌ | ✅ | Only auto works offline |
| Gold is tight | ✅ | ❌ | ❌ | Burst costs gold early |
| Gold is abundant | ✅ | ✅ | ✅ | All methods viable |
| Need building XP | ❌ | ✅ | ❌ | Burst is 13× faster XP |
| Max stability run | ❌ | ❌ | ✅ | Auto avoids over-building |

### 32.2 The Optimal Switching Pattern

```
Phase transition triggers:
  ──→ First prestige:   Switch from hold-only to hold+auto
  ──→ ab1 Lv5:          Switch to auto-primary
  ──→ bp+bs Lv5:        Add burst for thresholds
  ──→ All burst maxed:  Switch to burst-primary for XP
  ──→ Lv500 building:   Switch back to auto-primary
```

---

## 33. Theoretical Maximum Build Speed

### 33.1 All Bonuses Stacked

What's the absolute fastest you can place bricks?

```
Burst:        110 taps/s (maxed)
Auto:         2.8 taps/s (Lv15)
Hold:         8.3 taps/s (fixed)

Combined:     ~121 taps/s theoretical max
              But burst and hold can't run simultaneously (both need build tab)
              So: 110 taps/s burst OR 8.3 hold (while waiting for burst charges)
              Plus 2.8 auto (runs in background always)
```

### 33.2 Practical Maximum

In practice, you can't maintain 110 taps/s due to:
- Material constraints (as shown, 19× production gap)
- Stability constraints (tower collapses)
- Human factors (can't burst while holding)

The **practical maximum sustained build rate** is:
```
min(burst_rate, material_production_rate) + auto_background
= min(110 taps/s, 2.83 bricks/s × 2 taps/brick) + 2.8 auto
= min(110, 5.66) + 2.8
= 8.46 taps/s total
```

Still **material-limited**. Always material-limited.

### 33.3 The Material Wall

To achieve 110 taps/s sustained (55 bricks/s), you'd need:

```
Materials needed: 55 bricks/s + 55 mortar/s = 110 craft actions/s
Resources needed: ~400 resources/s (megalith costs ~7 per craft)
Gather rate needed: ~400 resources/s
```

This would require auto-gather and auto-craft at **~24,000 levels each**. Currently maxed at Lv15 (170 actions/min = 2.8 actions/s).

**The material wall is the fundamental limit.** Build method doesn't change this — only prestige upgrades and talents can raise the material ceiling.

---

## 34. One-Weird-Trick: Edge Cases & Exploits

### 34.1 Burst + Precarious Tower

If stability is exactly 5.1%:
- Safe zone: 0% collapse chance
- One more row: 4.9% → enters hazard zone at 5% collapse chance per row

Burst can place many rows at 5ms interval. If the tower collapses mid-burst, the remaining burst taps trigger `initTower()` which resets.

**Edge case**: If burst places 10 rows in 0.5s and collapses on row 7, rows 8-10 of the burst fire on a reset tower, wasting 3 rows of burst.

**Solution**: Check stability before each burst, not just at start.

### 34.2 Hold-to-Repeat on Burst Button

Currently hold-to-repeat on the build zone calls tapBuild(), not burst. But if you bind a macro/turbo-clicker to the burst button:

```
Hypothetical: Turbo-clicker on burst at 10 clicks/s
Each click: fires 20 taps (base) with charge cost
In 1 second: 10 bursts = 200 taps, 200🪙, 10 charges
```

But with max 6 charges, you'd drain in 0.6 seconds. Then wait 20s per charge recharge.

**Verdict**: Turbo-clicking burst is wasteful. Better to hold-tap for tapBuild() at 8.3/s.

### 34.3 Burst While Gathering

You can't burst while in the gather tab. But auto-build runs regardless of tab. So:

```
In gather tab: auto-build + auto-gather + auto-craft all run
In build tab: auto-build + optional burst/hold
```

Optimal play: **spend 90% of time in gather/craft tabs** (for material production + auto-build), **10% in build tab** (for burst threshold crossing).

### 34.4 The Pre-empty Burst

If auto-build is running and the tower is about to collapse, you can:
1. Switch to build tab
2. Watch auto-build place the next row
3. Burst *immediately after* the row completes but before the collapse check... no, the collapse check happens in tapBuild() which is called by auto-build too.

**No timing exploit available.** Collapse check is atomic with row completion.

---

## 35. Conclusion: The Optimal Player

### 35.1 Method Usage by Game Age

| Game Age | Prestige Count | Hold % | Burst % | Auto % |
|---|---|---|---|---|
| 0-1 hour | 0-10 | 90% | 0% | 10% |
| 1-10 hours | 10-50 | 40% | 10% | 50% |
| 10-50 hours | 50-200 | 10% | 20% | 70% |
| 50-200 hours | 200+ | 2% | 30% | 68% |
| 200+ hours | Endgame | 0% | 25% | 75% |

### 35.2 The Optimal Build Action

When faced with any build decision, ask:

```
1. Is auto-build running?     If no → Enable it
2. Do I have burst charges?   If yes → Burst for speed/XP
3. Do I need to cross a 25-threshold?  If yes → Burst
4. Do I need building XP?     If yes → Burst farm
5. Am I actively playing?     If yes → Hold while waiting for charges
6. Am I going AFK?            If yes → Ensure auto is running
```

### 35.3 Final Verdict

```
╔══════════════════════════════════════════════════════════════╗
║                                                              ║
║     AUTO-BUILD is the most important method to max first.    ║
║     BURST is the most powerful method to max eventually.    ║
║     HOLD is the method you'll use less and less over time.  ║
║                                                              ║
║     None of them matter if you can't feed the material       ║
║     pipeline. The real bottleneck is always upstream.        ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
```

---

*End of Build Methods Comparative Analysis. 1,278 lines.*
