# Babel — Temporal Dynamics & Speed Optimization

> **Optimization Problem**: Given the game's 100ms tick cycle, 120ms hold-to-repeat, 5ms burst interval, and automation at 0.35-2s cycles, what is the fastest path from zero to each goal?
> 
> **Core insight**: Time is the only non-renewable resource. Every action choice is a time allocation decision across mutually exclusive tabs.

---

## Table of Contents

1. [The Tick Economy](#1-the-tick-economy)
2. [Action Speed Benchmarking](#2-action-speed-benchmarking)
3. [Input Method Efficiency](#3-input-method-efficiency)
4. [Automation Breakpoint Analysis](#4-automation-breakpoint-analysis)
5. [Burst Timing Strategy](#5-burst-timing-strategy)
6. [Tab Switching & Opportunity Cost](#6-tab-switching--opportunity-cost)
7. [Prestige Cycle Optimization](#7-prestige-cycle-optimization)
8. [Pareto-Optimal Milestone Paths](#8-pareto-optimal-milestone-paths)
9. [Offline Efficiency](#9-offline-efficiency)
10. [Time-to-Mastery Projections](#10-time-to-mastery-projections)
11. [The Speedrunning Bracket](#11-the-speedrunning-bracket)
12. [Design Spec: Upgradeable Burst Engine](#12-design-spec-upgradeable-burst-engine)
13. [Design Spec: Dynamic Hold-to-Build](#13-design-spec-dynamic-hold-to-build)

---

## 1. The Tick Economy

### 1.1 The Game Loop

```
setInterval(callback, 100ms)
  ├── autoTick()       — idle pool accumulation
  ├── runAuto()        — automation dispatch (gather/craft/build)
  ├── S.tick++         — global tick counter
  └── if(tick%5===0)   — updateUI() throttled to 500ms
```

Each tick is **100ms** of real time. The game processes in lockstep with this clock:

| Event | Timing | Notes |
|---|---|---|
| Hold-to-repeat | Every 120ms | Independent of tick loop |
| Build burst | Every 5ms | Runs independent setTimeout chain |
| UI update | Every 500ms | `tick % 5 === 0` |
| Auto-save | Every 5,000ms | 50 ticks |
| Canvas draw | Every frame (~16ms) | Independent requestAnimationFrame |

### 1.2 The Critical Path

The player can only be in **one tab at a time**. Every second spent in Gather is a second not spent in Craft or Build. This creates a **trilemma**:

```
Time Allocation Problem:
  Maximize:  progress_rate(t)
  Subject:   t_gather + t_craft + t_build + t_skills + t_talents + t_ascend = t_total
```

At 8.3 actions/sec (hold-to-repeat), a minute of focused tapping produces ~500 actions. The game has ~25,000+ actions worth of content before first prestige. Time allocation efficiency can easily vary by 2-3× between optimal and naive play.

### 1.3 Tick-Aligned Automation

The automation system is tick-aligned:

```js
if(S.tick % (gi/100) < 1) { auto_action(); }
```

With the fixed `getAutoInterval()` returning `max(100, 3000/(1+l*0.5))`:

| Auto Level | Interval (ms) | Tick Alignment | Actions/Min |
|---|---|---|---|
| 1 | 2,000 | Every 20 ticks | 30 |
| 3 | 1,200 | Every 12 ticks | 50 |
| 5 | 857 | ~Every 8.6 ticks | 70 |
| 10 | 500 | Every 5 ticks | 120 |
| 15 | 353 | ~Every 3.5 ticks | 170 |

With p5 (Eternal Workshop, Lv3), effective level = purchased + 3:
| Purchased | Effective | Interval | Actions/Min |
|---|---|---|---|
| 1 | 4 | 1,000ms | 60 |
| 5 | 8 | 600ms | 100 |
| 10 | 13 | 381ms | 157 |

---

## 2. Action Speed Benchmarking

### 2.1 Raw Throughput by Input Method

| Method | Interval | Actions/sec | Actions/min | Notes |
|---|---|---|---|---|
| Hold-to-repeat | 120ms | 8.33 | 500 | After balance fix |
| Build burst | 5ms | 200 | 12,000 | Burst-limited to 200 actions |
| Automation Lv1 | 2,000ms | 0.5 | 30 | Base auto |
| Automation Lv15 | 353ms | 2.83 | 170 | Max auto |
| Auto + p5 Lv15eff | 300ms | 3.33 | 200 | With Eternal Workshop |
| Manual clicking | ~250ms | 4 | 240 | Human reaction limit |

### 2.2 Actions Per Goal

| Goal | Manual Actions | Time (manual, 8.3/s) | Time (burst, 200/s) | Time (auto Lv10) |
|---|---|---|---|---|
| Gather 100 stone | 100 | 12s | — | 50s |
| Craft 50 megaliths | 50 | 6s | — | 25s |
| Build 1 row (w=20) | 40 taps | 4.8s | 0.2s | 12s |
| Build 100 rows (w=20) | 4,000 taps | 8min | 20s burst cycles | 20min |

### 2.3 The Burst Advantage

Build burst at 200 taps/1sec is **24× faster** than hold-to-repeat (8.3 taps/sec) and **70× faster** than max automation (170/min). This makes burst the dominant build strategy — the limiting factor shifts from *build speed* to *material production*.

---

## 3. Input Method Efficiency

### 3.1 Efficiency Ratio: Actions per Human Effort

Define *human effort* as seconds of active attention:

| Method | Effort/sec | Output/sec | Efficiency (output/effort) |
|---|---|---|---|
| Hold-to-repeat (gather) | High | 8.3 actions | 8.3 |
| Hold-to-repeat (craft) | High | 8.3 actions | 8.3 |
| Burst (build) | Low (one tap) | 200 actions | 200 |
| Automation | None | 0.5-3 actions | ∞ |

**Insight**: Burst is so efficient relative to manual tapping that optimal play is:
1. Use auto for gather/craft (passive)
2. Burst for build (active, one tap)
3. Only manual-tap when auto hasn't produced enough materials

### 3.2 The Bottleneck Cascade

```
Gather (auto, 170/min) → Resources
    ↓
Craft (auto, 170/min) → Materials
    ↓
Build (burst, 12,000/min) → Tower Height
```

At max auto (Lv15 effective): 170 resources/min → craft 170 materials/min.

But burst consumes 20 materials + 20 mortar per row in 0.1 seconds. A 1-second burst (200 taps) consumes ~100 materials. At 170 materials/min, you can burst for **~1.7 seconds before running out**.

**The math**:
- Auto produces: 170 materials/min = 2.83/sec
- Burst consumes: 100 materials/sec
- Sustain ratio: 100 / 2.83 = **35:1 consumption ratio**

This means: for every 1 second of burst, you need 35 seconds of passive material accumulation.

---

## 4. Automation Breakpoint Analysis

### 4.1 Marginal Benefit of Auto Levels

```js
interval(l) = max(100, 3000 / (1 + 0.5 × l))
actions_per_min(l) = 60000 / interval(l)
```

| Level Change | Interval Δ | Actions/min Δ | Actions/min Δ/level |
|---|---|---|---|
| 0→1 | 3000→2000 | 20→30 (+10) | +10 |
| 1→2 | 2000→1500 | 30→40 (+10) | +10 |
| 2→3 | 1500→1200 | 40→50 (+10) | +10 |
| 3→4 | 1200→1000 | 50→60 (+10) | +10 |
| 4→5 | 1000→857 | 60→70 (+10) | +10 |
| 5→6 | 857→750 | 70→80 (+10) | +10 |
| 10→11 | 500→462 | 120→130 (+10) | +10 |
| 14→15 | 375→353 | 160→170 (+10) | +10 |

Each level adds exactly +10 actions/min. **Linear returns**.

### 4.2 Auto Upgrade Cost vs. Benefit

The cost grows geometrically while the benefit is linear:

| Auto | Level | Cost | Cumulative Cost | Benefit (act/min) | Cost per act/min |
|---|---|---|---|---|---|
| ag1 | 1 | 80 | 80 | +10 | 8.0 |
| ag1 | 5 | 492 | 1,289 | +50 | 25.8 |
| ag1 | 10 | 10,728 | 15,571 | +100 | 155.7 |
| ac1 | 1 | 120 | 120 | +10 | 12.0 |
| ac1 | 10 | 10,728 | 15,571 | +100 | 155.7 |
| ab1 | 1 | 200 | 200 | +10 | 20.0 |
| ab1 | 10 | 10,728 | 15,571 | +100 | 155.7 |

**Optimal auto investment**: Buy each to Lv3-5 early (good value), return to max later.

### 4.3 Automation Trilemma

You can automate gather, craft, and build — but each costs gold. Which auto system unlocks first?

| Priority | Rationale |
|---|---|
| **1. Auto-gather (ag1)** | Resources are the root of all production. Buy to Lv3 ASAP. |
| **2. Auto-craft (ac1)** | Converts resources to materials. Buy to Lv3 ASAP. |
| **3. Auto-build (ab1)** | Least critical — burst is 24× faster than auto-build anyway. |
| **4. p5 Eternal Workshop** | +3 levels to all, effective Lv4 from Lv1 purchases. |

### 4.4 p5 Efficiency

p5 (Eternal Workshop) at Lv3 gives +3 auto levels to all skills. This costs shards:

| Investment | Effect | Shard Cost | Alternative Gold Cost |
|---|---|---|---|
| p5 Lv1 | +1 all auto levels | 15 | ~5K gold in upgrades |
| p5 Lv3 | +3 all auto levels | 1,035 | ~50K+ gold |

Since each auto upgrade level costs ~10K+ gold at higher levels, p5 becomes extremely cost-effective after Lv5-6.

---

## 5. Burst Timing Strategy

### 5.1 Optimal Burst Windows

Burst builds 200 taps in 1 second. But the tower can collapse mid-burst. The stability check happens after each row completion.

With stability `p`:
- At high stability (p > 25%): burst is safe
- At moderate stability (10% < p < 25%): burst is risky
- At low stability (p < 10%): burst is dangerous

**Optimal burst windows** (after stability fix with <15% block):

| Tower Config | Optimal Burst Range | Notes |
|---|---|---|
| Width 20, base | 0-100 rows | Safe below 80% height/maxSafe |
| Width 20, all rf+fd | 0-140 rows | Greatly extended safe zone |
| Width 30, all upgrades | 0-160 rows | Wide + reinforced |
| Width 50, all upgrades | 0-240 rows | Max width, max safety |

### 5.2 Burst Discipline

**Rule of thumb**: Burst only when `stability > 25%`. Above this threshold, the risk of catastrophic collapse during the 1-second burst window is near zero.

**The Collapse Tax**: A collapsed tower at height 200 loses:
- ~200 rows of build progress
- ~1-2 minutes of material production
- ~4,000 resources worth of materials

But awards shards + legacy. So collapse isn't pure loss — it's **forced prestige**. The question is whether the collapse happened at optimal or suboptimal height.

### 5.3 Burst for Speed vs. Burst for Safety

| Strategy | When to Burst | Shards/Hour | Risk |
|---|---|---|---|
| Aggressive | Always | High (target: cycles < 2min) | May collapse sub-optimally |
| Conservative | Only > 50% stability | Medium-high | Fewer wasted cycles |
| Manual-only | Never | Medium | Zero collapse waste |

### 5.4 Burst as a Material Sink

A single burst consumes: `100 taps = 50 bricks = 50 materials + 50 mortar`
At width 20, that's 2.5 rows per burst.

Material requirements for burst:
| Burst Duration | Actions | Materials Needed | Mortar Needed |
|---|---|---|---|
| 1s (200 taps) | 200 | 100 | 100 |
| 2s (400 taps) | 400 | 200 | 200 |
| 5s (1000 taps) | 1000 | 500 | 500 |

---

## 6. Tab Switching & Opportunity Cost

### 6.1 The Tab Lock

You can only be in one tab at a time. Automation runs in the background regardless, but active tapping is exclusive.

### 6.2 Optimal Tab Time Allocation

**First 30 seconds of a fresh run**:

| Time | Tab | Actions | Rationale |
|---|---|---|---|
| 0-5s | Gather | ~42 gather taps | Stockpile initial resources |
| 5-10s | Craft | ~42 craft taps | Convert to mortar + bricks |
| 10-30s | Build | ~167 build taps (burst) | Build height, each tap gives XP |

**Mid-run (after auto established)**:

| Time | Tab | Actions | Rationale |
|---|---|---|---|
| 0-10s | Build | 200-tap burst | Consume all accumulated materials |
| 10-20s | Skills | ~83 taps | Gold + general XP while materials recharge |
| 20-60s | Any | Hold-to-repeat | Let auto replenish materials |

### 6.3 Opportunity Cost of Skills/Talents/Ascend Tabs

These tabs give gold with no resource consumption — they're "free" in material terms. But they consume your active attention.

| Tab | Gold/sec | XP/sec | Opportunity Cost |
|---|---|---|---|
| Skills | ~6.25 gold/s | 8.3 gen XP/s | Could be gathering 8.3 resources + gold |
| Talents | ~12.5 gold/s | 0 | Could be crafting materials + gold |
| Ascend | ~12.5 gold/s + shard chance | 0 | Same as talents |

**Verdict**: Skills tab is worth visiting for XP grind. Talents/Ascend tabs are only worth it if you need gold immediately and can't gather/craft (e.g., you have no resources).

### 6.4 Optimal Respec Cycle

If a "respec" (talent refund) is available, the optimal cycle might be:
1. Build tall → collapse → get shards
2. Respec from build-focused talents → gold-focused talents
3. Grind gold to buy techs
4. Respec back

---

## 7. Prestige Cycle Optimization

### 7.1 Cycle Time Model

```
cycle_time = time_to_build + time_to_collapse + time_to_buy_upgrades

time_to_build ≈ tower_height × bricks_per_row × 2 taps / burst_rate
time_to_collapse ≈ 0 (instant, on failure)
time_to_buy_upgrades ≈ 10-60s of gold grinding
```

### 7.2 Optimal Collapse Height

The shard payoff function is stepwise:
```
shards(h) = floor(h/25) + floor(legacy/10)
```

Shards-per-hour is maximized at a specific height range (diminishing returns on tall builds):

| Collapse Height | Shards | Build Time (est.) | Shards/Hour |
|---|---|---|---|
| 25 | 1 | 30s | 120 |
| 50 | 2 | 90s | 80 |
| 75 | 3 | 3min | 60 |
| 100 | 4 | 5min | 48 |
| 150 | 6 | 10min | 36 |
| 200 | 8 | 15min | 32 |
| 300 | 12 | 30min | 24 |

**Optimal cycle**: Short runs to height 25-50 for shard/hour maximization early on. Longer runs (200+) only when legacy is high enough to contribute meaningful bonus shards.

### 7.3 Legacy Amplification

Legacy resets: `legacy = max(old, floor(tallest × (0.1 + p4_lvl × 0.005)))`

Legacy growth accelerates over time:
| Cycle | Tallest | p4 | Legacy | Legacy Shards | Total Shards |
|---|---|---|---|---|---|
| 1 | 50 | 0 | 5 | 0 | 2 |
| 5 | 100 | 3 | 25 | 2 | 6 |
| 10 | 200 | 5 | 70 | 7 | 15 |
| 20 | 300 | 5 | 105 | 10 | 22 |
| 50 | 400 | 5 | 140 | 14 | 30 |

### 7.4 The 60-Second Prestige

With max width, high auto levels, and burst:
1. Start with auto gathering/crafting (passive)
2. One burst to height 25 (0.5 seconds)
3. Wait for collapse or tap bricks until collapse
4. Collect 2-3 shards
5. Repeat

This creates a **sub-60 second prestige loop**. At 3 shards per 60s = 180 shards/hour. All prestige maxed in ~227 hours.

---

## 8. Pareto-Optimal Milestone Paths

### 8.1 Fastest Path to Lv500 Gathering

1. Focus all taps in Gather tab
2. Buy G1-G4, R1-R6, SG1-SG3 early
3. Use auto-gather to supplement
4. Estimated: **8-12 hours** continuous play (without debug)

With DB=10: **45-75 minutes**

### 8.2 Fastest Path to Lv500 Crafting

1. Let auto-gather build resources
2. Focus active taps in Craft tab
3. Buy C1-C4, SC1-SC3
4. Estimated: **10-15 hours** (craft XP lags behind gather because fewer actions)

### 8.3 Fastest Path to Lv500 Building

1. Burst-build constantly
2. Each burst is 200 taps × 2 XP = 400 building XP
3. With DB=10 and ×50 XP multipliers: 20K XP per burst
4. Need 270M XP for Lv500 → 13,500 bursts → **~4 hours** with DB

Without DB: **~40 hours**

### 8.4 Fastest Path to Lv500 General

General XP is 50% of all skill XP. It naturally follows the other three. Focus on:
1. All three skills equally (balanced approach)
2. Buy all SG/SC/SB upgrades
3. Skills tab tapping for pure general XP

### 8.5 Pareto Frontier: Multiple Goals

```
Goal: Lv500 all skills + max prestige
Fastest path:
├── Phase 1 (0-2h): Reach Lv50 all skills, first prestige
├── Phase 2 (2-8h): Grind to Lv200 all skills, buy all tech
├── Phase 3 (8-24h): Push Lv500 gathering + crafting via auto
├── Phase 4 (24-48h): Prestige loops for shards
└── Phase 5 (48h+): Lv500 building via burst cycles
```

---

## 9. Offline Efficiency

### 9.1 Offline Progress Mechanics

```js
const ticks = Math.min(elapsed_ms, 86400000) / 100;
autoGathers = Math.floor(ticks / (gi/100));  // at gi interval
autoCrafts = Math.floor(ticks / (ci/100));   // at ci interval
autoBuilds = Math.floor(ticks / (bi/100));   // at bi interval, capped at 500 rows
```

### 9.2 Offline Gains at Different Auto Levels

| Auto Level | 1 Hour Offline | 8 Hours Offline | 24 Hours Offline |
|---|---|---|---|
| Lv1 (2s interval) | 1,800 actions | 14,400 | 43,200 |
| Lv5 (0.86s) | 4,186 | 33,488 | 100,464 |
| Lv10 (0.5s) | 7,200 | 57,600 | 172,800 |
| Lv15 (0.35s) | 10,200 | 81,600 | 244,800 |

### 9.3 Offline Build Cap

Auto-build is capped at 500 rows regardless of time. After 500 rows, the tower would collapse from instability. This cap is reached in:
- Lv1 auto-build: ~16 minutes
- Lv10 auto-build: ~4 minutes
- Lv15 auto-build: ~3 minutes

### 9.4 Optimal Play/Save Cadence

Given the 500-row auto-build cap, checking in every **5-10 minutes** during active play periods maximizes offline build value. Overnight (8h), most value comes from auto-gather and auto-craft, not build.

---

## 10. Time-to-Mastery Projections

### 10.1 All Milestones (Lv500 all skills)

| Method | Gather | Craft | Build | General | Total |
|---|---|---|---|---|---|
| Manual only (8.3/s) | 30h | 40h | 60h | 45h | **175h** |
| Optimal burst/auto | 12h | 15h | 20h | 15h | **62h** |
| With DB=10 | 1.2h | 1.5h | 2h | 1.5h | **6.2h** |

### 10.2 All Prestige Max

| Method | Shards/Hour | Time to 40K Shards |
|---|---|---|
| Early game (5 shards/cycle, 5min) | 60 | 667h |
| Mid game (15 shards/cycle, 3min) | 300 | 133h |
| Late game (30 shards/cycle, 2min) | 900 | 44h |
| Optimal (60s prestige, 3 shards) | 180 | 227h |

### 10.3 All Talents (500M gold)

| Method | Gold/Hour | Time |
|---|---|---|
| Manual tapping (8.3/s, 500 gold/s) | 1.8M | 278h |
| Mid-game auto (5000 gold/s) | 18M | 28h |
| Late-game (50K gold/s) | 180M | 2.8h |

### 10.4 Everything Maxed

```
Ultimate completion time (optimal play, no debug):
├── First prestige: 3 min
├── All milestone skills Lv500: 62h
├── All tech: 6h (done during skill grind)
├── All skill upgrades: 4h (done during skill grind)
├── All auto upgrades: 6h (done during skill grind)
├── All prestige (40K shards): 133h
├── All talents (500M gold): 28h (or done during shard grind)
└── Total: ~200-240 hours of active play → ~8-10 days
```

---

## 11. The Speedrunning Bracket

### 11.1 Category: First Collapse (Any%)

| Strategy | Time | Taps | Key Actions |
|---|---|---|---|
| Naive | ~3min | ~1,000 | Tap gather → craft → build linearly |
| Optimized | ~45s | ~300 | Skill tab for gold → buy g1/c1 → burst |
| Theoretical minimum | ~15s | ~200 | Perfect burst use, pre-crafted materials |

### 11.2 Category: Lv10 All Skills (Any%)

Theoretical minimum: **~5 minutes** with optimal burst cycling.

### 11.3 Category: First Megalith (Crafting Lv18)

Theoretical minimum with optimal XP routing: **~2 hours**.

---

## 12. Design Spec: Upgradeable Burst Engine

### 12.1 Concept

The current burst system is binary (always 200 taps at 5ms). An upgradeable burst engine adds strategic depth: invest gold/resources to make burst faster, more powerful, or more sustainable.

### 12.2 Variables

| Variable | Base Value | Description | Upgrade Effect |
|---|---|---|---|
| **Power** | 1 brick/tap | Bricks placed per burst action | +1/tap per level |
| **Speed** | 5ms/action | Milliseconds between burst actions | -0.5ms per level (min 1ms) |
| **Max Reserve** | 200 actions | Max burst actions available | +50 per level |
| **Recovery Delay** | 3s | Seconds before reserve starts refilling | -0.5s per level (min 0.5s) |
| **Recovery Rate** | 10/s | Actions recovered per second | +5/s per level |
| **Burst Cap** | 200 taps | Hard max per burst click | +50 per level |

### 12.3 How It Works

The burst engine has a **reserve** (like stamina):

```
Reserve starts at max (e.g., 200)
  ↓
Tap burst → drains reserve at speed× power
  ↓
Reserve empty → burst stops
  ↓
Recovery delay → reserve begins refilling
  ↓
Reserve full → ready for next burst
```

### 12.4 Upgrade UI

A dedicated "Burst Engine" sub-panel in the Build tab showing:

```
╔═══════════════════════════════════╗
║       ⚡ BURST ENGINE              ║
║  Reserve: ████████░░░░ 142/200     ║
║  Status: Recharging (1.2s left)   ║
║                                    ║
║  Power: Lv.3  (+2 bricks/tap)     ║ ⬆ 1,200🪙
║  Speed: Lv.5  (2.5ms/action)      ║ ⬆ 3,500🪙
║  Reserve: Lv.2 (300 max)          ║ ⬆ 800🪙
║  Recovery: Lv.1 (15/s, 2.5s del)  ║ ⬆ 500🪙
╚═══════════════════════════════════╝
```

### 12.5 Strategic Implications

- **Burst Power**: Higher power means fewer taps to place a row → less time spent in build tab
- **Burst Speed**: Faster actions → less real-time per burst → more burst cycles per minute
- **Reserve**: More actions per burst → longer continuous building
- **Recovery**: Faster recovery → more frequent bursts → higher sustained build rate

**Optimal build for speed builds**: Max Power + Max Speed first (burst is a sprint)
**Optimal build for AFK builds**: Max Reserve + Max Recovery first (burst becomes a marathon)

---

## 13. Design Spec: Dynamic Hold-to-Build

### 13.1 Concept

Hold-to-repeat currently fires at a fixed 120ms interval. A dynamic system adds a **warm-up** mechanic: the longer you hold, the faster you build — until you reach peak speed.

### 13.2 Variables

| Variable | Base Value | Description | Upgrade Effect |
|---|---|---|---|
| **Power** | 1 brick/action | Bricks placed per hold action | +1 per level |
| **Initial Speed** | 120ms | Starting interval at first tap | -10ms per level (min 40ms) |
| **Acceleration** | 5ms/s | Interval decreases per second held | -1ms/s per level |
| **Warm-up Time** | 5s | Seconds to reach min interval | +1s per level |
| **Min Interval** | 40ms | Fastest possible speed | -3ms per level (min 10ms) |

### 13.3 How It Works

```
Hold starts: interval = 120ms
  ↓
After 1s: interval = 115ms (120 - 5)
After 2s: interval = 110ms
After 3s: interval = 105ms
  ...
After 5s: interval = 40ms (min)
  ↓
Release → interval resets to 120ms
```

### 13.4 Upgrade UI

A dedicated "Hold Technique" sub-panel:

```
╔═══════════════════════════════════╗
║     🖐️ HOLD TECHNIQUE              ║
║  Current speed: ████░░░░ 85ms      ║
║  Warm-up: [=========>-------] 62%  ║
║                                    ║
║  Power: Lv.2 (+1 brick/action)     ║ ⬆ 1,500🪙
║  Initial: Lv.3 (90ms start)        ║ ⬆ 2,000🪙
║  Warm-up: Lv.1 (6s to peak)        ║ ⬆ 800🪙
║  Peak: Lv.2 (34ms min)             ║ ⬆ 2,500🪙
╚═══════════════════════════════════╝
```

### 13.5 Strategic Implications

- **Short bursts (<2s hold)**: Initial speed matters most
- **Long holds (5s+)** : Acceleration + warm-up time + min interval matter most
- **Optimal pattern**: Hold for 5s to reach peak speed, release, re-hold. Each cycle gives ~25 actions at increasing speed.
- **Power upgrades**: Every hold action places more bricks → effective actions/second increases dramatically

### 13.6 Comparison: Burst vs. Hold

| Feature | Burst | Hold |
|---|---|---|
| Peak speed | 200 actions/s | ~50 actions/s (at max upgrade) |
| Sustainability | Limited by reserve | Unlimited (no resource cost) |
| Attention required | One tap per burst | Continuous holding |
| Best for | Sprint building | Steady construction |
| Upgrade focus | Power + Reserve + Recovery | Power + Acceleration + Min Speed |

---

*End of Temporal Dynamics Analysis. Companion file: babel_stochastic_analysis.md*
