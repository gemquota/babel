# Babel — Complete Theorycrafting Economic Analysis

> **Game**: Tower of Babel incremental game  
> **File**: `index.html` (~1310 lines, single-file HTML/CSS/JS)  
> **Repo**: https://github.com/gemquota/babel  
> **Deployed**: https://gemquota.github.io/babel/  
> **Author**: gemquota  
> **Analysis Date**: 2026-07-14

---

## Table of Contents

1. [Overview of Economic Systems](#1-overview-of-economic-systems)
2. [Currency Hierarchy & Sinks](#2-currency-hierarchy--sinks)
3. [The Four Skill XP Tracks](#3-the-four-skill-xp-tracks)
4. [Milestone System](#4-milestone-system)
5. [Resource Economy (Gather)](#5-resource-economy-gather)
6. [Material Economy (Craft)](#6-material-economy-craft)
7. [Tower Building Economy (Build)](#7-tower-building-economy-build)
8. [Upgrade Progression Path](#8-upgrade-progression-path)
9. [Talent Tower Analysis](#9-talent-tower-analysis)
10. [Prestige & Collapse Economics](#10-prestige--collapse-economics)
11. [Stability Formula Deep Dive](#11-stability-formula-deep-dive)
12. [Multiplier Stacking & Synergies](#12-multiplier-stacking--synergies)
13. [Cost Scaling Models](#13-cost-scaling-models)
14. [Production Rate Analysis](#14-production-rate-analysis)
15. [Optimal Strategies](#15-optimal-strategies)
16. [Bottleneck Analysis](#16-bottleneck-analysis)
17. [Growth Curves & Time-to-Completion](#17-growth-curves--time-to-completion)
18. [Balance Recommendations](#18-balance-recommendations)
19. [Glossary of Formulae](#19-glossary-of-formulae)

---

## 1. Overview of Economic Systems

Babel has **5 distinct currencies**, **3 core XP tracks**, **1 general XP track**, and a **prestige layer**. All systems interact through a nested production chain:

```
Gather ─→ Resources ─→ Craft ─→ Materials ─→ Build ─→ Tower Height ─→ Collapse ─→ Shards
   │                      │                     │
   ├── Gold ──────────────┼─────────────────────┼──→ Gold sinks (upgrades, tech, talents)
   │                      │                     │
   └── Gather XP ──────→ Craft XP ───────────→ Build XP ──→ General XP (50% of each)
```

**Currency Table:**

| Currency | Symbol | Earned By | Spent On | Hard Cap |
|---|---|---|---|---|
| Gold | 🪙 | All actions, tap zones | Upgrades, Tech, Talents, Init | No |
| Resources | R (🟤) | Gather tab | Crafting recipes | No |
| Materials | 🧱 | Craft tab | Building tower | No |
| Babel Shards | 💎 | Tower collapse | Prestige upgrades | No |
| Legacy | % | Tower collapse | ×XP multiplier (passive) | No |

---

## 2. Currency Hierarchy & Sinks

### 2.1 Gold (🪙) — Primary Medium of Exchange

**Earning rates** (per tap, with Debug ×10):

| Source | Base Gold | Formula |
|---|---|---|
| Gather tap | 1 × DB | `max(1, floor(1 * (1 + 0.5*g1_lv + 1*g2_lv + 2*g3_lv + 4*g4_lv))) * (1 + p7*0.5)` |
| Craft tap | material.tier × DB | `floor(mat.t * (1 + 0.5*c1 + 1*c2 + 2*c3 + 4*c4)) * (1 + p7*0.5)` |
| Build tap (place) | 1-3 × DB | `floor(Math.random()*3 + 1) * DB` |
| Skills tap | 1-2 × DB | `max(1, floor(Math.random()*2 + 1)) * DB * (1 + p7*0.5)` |
| Talents tap | 2-4 × DB | `max(1, floor(Math.random()*3 + 2)) * DB * (1 + t5*0.15) * (1 + p7*0.5)` |
| Ascend tap | 0-5 × DB | `floor(Math.random()*5 + 1) * DB` |

**Total Gold Sinks (ordered by unlock):**

| Sink | Total Levels | Total Cost (gold) | Cost Model |
|---|---|---|---|
| G1-G4 (gather) | 10 each = 40 | ~35,533 | `20×2.5^lvl` → `1000×3.5^lvl` |
| C1-C4 (craft) | 10 each = 40 | ~63,071 | `25×2.5^lvl` → `1500×3.5^lvl` |
| R1-R6 (resource) | 15 each = 90 | ~5,945,718 | `50×2.8^lvl` → `50000×5^lvl` |
| SG1-SG3 (skill ×2-5) | 10 each = 30 | ~441,806 | `100×2.5^lvl` → `20000×5^lvl` |
| SC1-SC3 (skill ×2-5) | 10 each = 30 | ~441,806 | Same as SG |
| SB1-SB3 (skill ×2-5) | 10 each = 30 | ~441,806 | Same as SG |
| AG1-AB3 (auto) | 10 each = 90 | ~323,984 | `80×2.8^lvl` → `8000×3.8^lvl` |
| Tech (6 width + 5 rf + 3 fd) | 14 total | ~937,800 | Linear/stepped |
| 16 talents × 10 levels | 160 total | ~5,714,286+ | `cb×cm^lvl`, cb 80-10000, cm 2.2-5 |

**Total Gold Required for ALL content**: ~14M+ gold (without considering compound scaling of late upgrade levels)

### 2.2 Resources (R) — Consumable Feedstock

**8 resource types**, unlocked by gathering level:

| Resource | Unlock Level | Gather Level Source | Used In |
|---|---|---|---|
| Mud 🟤 | 0 | Gatherable at Lv1 | Mud Brick (mud:2, straw:1) |
| Water 💧 | 0 | Gatherable at Lv1 | Mortar (sand:2, water:1, lime:1), Fired Brick (clay:2, sand:1, water:1), Glazed Brick |
| Straw 🌾 | 0 | Gatherable at Lv1 | Mud Brick (mud:2, straw:1) |
| Gravel 🪨 | 2 | Lv2+ | — (currently unused in crafting!) |
| Sand 🏖️ | 3 | Lv3+ | Mortar, Fired Brick, Glazed Brick |
| Clay 🧱 | 4 | Lv4+ | Fired Brick (clay:2, sand:1, water:1) |
| Lime 🪨 | 5 | Lv5+ | Mortar, Reinforced Brick |
| Stone ⛰️ | 7 | Lv7+ | Stone Block (stone:3), Reinforced Brick |

**Note**: Gravel is gathered but has *no current crafting use* — it is a dead-end resource.

### 2.3 Materials — Intermediate Goods

**7 material types**, unlocked by crafting level:

| Material | Unlock | Cost | Tier | Strength |
|---|---|---|---|---|
| Mortar 🧴 | Lv0 | sand:2, water:1, lime:1 | 2 | — |
| Mud Brick 🧱 | Lv0 | mud:2, straw:1 | 2 | 1.0 |
| Fired Brick 🔥 | Lv3 | clay:2, sand:1, water:1 | 4 | 0.8 |
| Stone Block 🗿 | Lv6 | stone:3 | 5 | 0.6 |
| Reinforced Brick ⚔️ | Lv8 | firedBrick:1, stone:1, lime:1 | 5 | 0.4 |
| Glazed Brick ✨ | Lv12 | firedBrick:1, sand:2, water:1 | 6 | 0.3 |
| Megalith 🏛️ | Lv18 | stoneBlock:2, reinfBrick:1 | 8 | 0.2 |

Material strength is inverted — lower = better (less strain on tower stability).

### 2.4 Babel Shards (💎) — Prestige Currency

**Earning formula:**
```js
shards = Math.floor(height / 25) + Math.floor(legacy / 10)
```
Where `legacy = Math.floor(tallest * (0.1 + p4_lvl * 0.005))`

**7 prestige upgrades**, each with increasing shard cost:

| Upgrade | Effect | Max Level | Base Cost | Multiplier |
|---|---|---|---|---|
| p1 — Diligent Start | +100 starting gold | 10 | 1 | 2.2 |
| p2 — Wider Legacy | +1 base width | 5 | 3 | 3 |
| p3 — Ancient Foundation | +3% stability | 5 | 5 | 3 |
| p4 — Echoes of Labor | +0.5%/lv legacy | 5 | 8 | 3.5 |
| p5 — Eternal Workshop | +1 auto level | 3 | 15 | 4 |
| p6 — Babel's Memory | +5 per resource | 5 | 10 | 3.5 |
| p7 — Golden Legacy | +50%/lv gold | 5 | 20 | 4 |

**Total shards to max all**: ~40,779 shards (with some variation)

---

## 3. The Four Skill XP Tracks

### 3.1 XP Requirement Function

```js
xpN(lv) = floor(50 * lv * (1 + 0.12 * lv))
```

**XP Table (selected levels):**

| Level | XP Required | Cumulative XP | Equivalent Actions (×1) | Equivalent Actions (×10, DB=10) |
|---|---|---|---|---|
| 1 | 56 | 56 | 56 | 6 |
| 5 | 400 | 1,200 | 1,200 | 120 |
| 10 | 1,100 | 5,775 | 5,775 | 578 |
| 25 | 5,000 | 68,750 | 68,750 | 6,875 |
| 50 | 17,500 | 388,750 | 388,750 | 38,875 |
| 75 | 37,500 | 1,228,750 | 1,228,750 | 122,875 |
| 100 | 65,000 | 2,868,750 | 2,868,750 | 286,875 |
| 125 | 100,000 | 5,608,750 | 5,608,750 | 560,875 |
| 150 | 142,500 | 9,758,750 | 9,758,750 | 975,875 |
| 200 | 250,000 | 22,733,750 | 22,733,750 | 2,273,375 |
| 250 | 387,500 | 42,658,750 | 42,658,750 | 4,265,875 |
| 300 | 555,000 | 70,283,750 | 70,283,750 | 7,028,375 |
| 400 | 980,000 | 148,658,750 | 148,658,750 | 14,865,875 |
| 500 | 1,525,000 | 270,433,750 | 270,433,750 | 27,043,375 |

### 3.2 XP Income Rates

**Base XP per action (before multipliers):**

| Action | Skill XP | General XP |
|---|---|---|
| Gather tap | 1×DB | 0.5×DB |
| Craft tap | 2×DB | 1×DB |
| Build tap (position) | 1×DB | — |
| Build tap (place) | 2×DB | 1×DB |
| Skills tab tap | — | 1×DB |
| Talents tab tap | — | — |
| Ascend tab tap | — | — |

### 3.3 XP Multiplier Stacking

The `earnX(skill, base)` function applies these multipliers in order:

```
earnX multiplers:
1.  ×2 if general milestone ≥2 claimed
2.  ×4 if general milestone ≥8 claimed
3.  ×(1 + sg1_lvl) for gathering
    ×(1 + sc1_lvl) for crafting
    ×(1 + sb1_lvl) for building
4.  ×(1 + d1_lvl × 0.15) from Divine Inspiration talent
5.  ×(1 + legacy × 0.01) from accumulated legacy
```

**Maximum theoretical XP multiplier per skill:**

| Source | Max Multiplier |
|---|---|
| General milestone 2 | ×2 |
| General milestone 8 | ×4 |
| SG1 (gathering skill upgrade) | ×11 (Lv10, +1 per level = +1000%? wait...) |

Actually the skill upgrades work like:
```js
const v = uL("sg1"); if(v > 0) m *= 1 + v
```
So `sg1` at Lv10 gives `×11` (1 + 10). Similarly sc1/sb1.

| d1 talent | `×(1 + 10 × 0.15) = ×2.5` |
|---|---|
| Legacy at 500% | `×(6.0)` |
| **Total (gathering)** | **2 × 4 × 11 × 2.5 × 6 = ×1320** |

Note: DB=10 multiplies *base* XP, then these multipliers compound on top.

---

## 4. Milestone System

### 4.1 Structure

4 milestone tracks (gathering, crafting, building, general), each with 13 tiers:
- Levels 5, 10, 25, 50, 75, 100, 125, 150, 200, 250, 300, 400, 500

Only the next unclaimed milestone is visible until claimed.

### 4.2 Milestone Bonuses (applied globally)

| Track | Milestone | Bonus |
|---|---|---|
| Gathering ≥1 | claimed at Lv5 | +30% gold per gather (`Math.round(g*(1+0.3*claimed))`) |
| Gathering ≥4 | claimed at Lv50 | +0.2 reinforce (tower stability) |
| Gathering ≥8 | claimed at Lv200 | +0.3 reinforce (tower stability) |
| Crafting ≥1 | claimed at Lv5 | +30% craft amount per |
| General ≥2 | claimed at Lv10 | ×2 XP multiplier |
| General ≥8 | claimed at Lv200 | ×4 XP multiplier |

### 4.3 Cumulative Benefits at Max Milestones (13/13 claimed per track)

| Track | Effect |
|---|---|
| Gathering | gold mult: `×(1+13×0.3) = ×4.9`, reinforce: +0.5 |
| Crafting | amount mult: `×(1+13×0.3) = ×4.9` |
| Building | (no active bonus attached currently) |
| General | XP mult: ×2 ×4 = ×8 (at 2 and 8 only) |

---

## 5. Resource Economy (Gather)

### 5.1 Base Gathering Rate

```js
gather yield = max(1, floor(
    base_yield × DB × (1 + Σ(r_multiplier × r_lvl))
))
```

Where `base_yield = 1`, `r_multiplier` ranges from 0.1 (r1) to 1.0 (r6).

**Resource Upgrades analysis:**

| Upgrade | Per Level | Max (Lv15) | Cumulative (all R upgrades) |
|---|---|---|---|
| r1 — Rustic Tools | +10% | +150% | — |
| r2 — Ox Cart | +15% | +225% | — |
| r3 — Water Wheel | +20% | +300% | — |
| r4 — Crane | +30% | +450% | — |
| r5 — Steam Engine | +50% | +750% | — |
| r6 — Magic Loom | +100% | +1500% | — |
| **Total** | — | — | **+3325% × gather_yield** |

**Effective gather yield with all Lv15 resource ups:**
```js
amount = floor(1 × DB × (1 + 33.25)) = floor(34.25 × DB) = 34 (or 342 with DB=10)
```

### 5.2 Gold from Gathering

```js
gAmt = max(1, floor(1 × (1 + 0.5×g1 + 1×g2 + 2×g3 + 4×g4))) × (1 + p7×0.5)
```

| g1 | g2 | g3 | g4 | Gold per Gather |
|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 1 × (1 + p7×0.5) |
| 10 | 0 | 0 | 0 | 6 × (1 + p7×0.5) |
| 10 | 10 | 0 | 0 | 17 × (1 + p7×0.5) |
| 10 | 10 | 10 | 0 | 57 × (1 + p7×0.5) |
| 10 | 10 | 10 | 10 | 137 × (1 + p7×0.5) |

With p7 at Lv5: `×(1+2.5) = ×3.5`

**Max gold per gather**: `137 × 3.5 = 479`

### 5.3 Resource Unlock Progression

Gathering skill level directly gates which resources are available:
- `gF()` picks the *highest unlocked* resource — you always gather the most advanced one
- This means early game: mud only → later: water+straw+mud → eventually: stone only
- Critical gap: **Gravel (Lv2)** is gathered but has **zero recipes** consuming it

---

## 6. Material Economy (Craft)

### 6.1 Auto-Craft Selection Algorithm

```js
autoCraft():
  1. Find all brick materials (non-mortar) with sufficient resources
  2. Prefer last selected craft (`S._selCraft`)
  3. Otherwise pick the highest-indexed (most advanced) brick
  4. Fall back to mortar if bricks unreachable
```

**Important**: This always crafts the *most advanced* material you can afford, not necessarily the most efficient one.

### 6.2 Craft Cost Analysis

**Resource cost per craft action:**

| Material | mud | straw | clay | sand | water | lime | stone | firedBrick | stoneBlock | reinfBrick |
|---|---|---|---|---|---|---|---|---|---|---|
| Mortar | 0 | 0 | 0 | 2 | 1 | 1 | 0 | 0 | 0 | 0 |
| Mud Brick | 2 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Fired Brick | 0 | 0 | 2 | 1 | 1 | 0 | 0 | 0 | 0 | 0 |
| Stone Block | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 | 0 | 0 |
| Reinforced Brick | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 1 | 0 | 0 |
| Glazed Brick | 0 | 0 | 0 | 2 | 1 | 0 | 0 | 1 | 0 | 0 |
| Megalith | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 1 |

### 6.3 Chain Complexity Increase

**Megalith production chain:**
```
1. Gather: sand (Lv3), clay (Lv4), lime (Lv5), stone (Lv7)
2. Craft firedBrick: clay:2 + sand:1 + water:1
3. Craft stoneBlock: stone:3
4. Craft reinfBrick: firedBrick:1 + stone:1 + lime:1
5. Craft megalith: stoneBlock:2 + reinfBrick:1
```

Total raw resources per megalith:
- clay: 2 (for firedBrick → reinfBrick → megalith... actually let me trace)

Let me trace the tree more carefully:

**1 megalith =** 2× stoneBlock + 1× reinfBrick  
**1 stoneBlock =** 3 stone  
**1 reinfBrick =** 1 firedBrick + 1 stone + 1 lime  
**1 firedBrick =** 2 clay + 1 sand + 1 water  

**Total raw per megalith:**
- stone: `3×2 + 1 = 7`
- clay: `2×1 = 2` (for the firedBrick in the reinfBrick)
- sand: `1×1 = 1`
- water: `1×1 = 1`
- lime: `1×1 = 1`

### 6.4 Craft Amount & Gold

```js
craft amount = max(1, DB × (1 + crafting_milestone_count × 0.3))

craft gold = max(1, floor(mat.t × (1 + 0.5×c1 + 1×c2 + 2×c3 + 4×c4))) × (1 + p7×0.5)
```

Material tier value (used for gold):
| Material | Tier | Base Gold |
|---|---|---|
| Mortar | 2 | 2 |
| Mud Brick | 2 | 2 |
| Fired Brick | 4 | 4 |
| Stone Block | 5 | 5 |
| Reinforced Brick | 5 | 5 |
| Glazed Brick | 6 | 6 |
| Megalith | 8 | 8 |

---

## 7. Tower Building Economy (Build)

### 7.1 The 2-Tap System

Each brick requires exactly **2 taps**:
1. **Position** (`st:'a'`): Brick hovers above with bobbing animation. Earns 1×DB building XP.
2. **Place** (`st:'d'`): Consumes 1 material + 1 mortar. Earns 2×DB building XP + 1-3×DB gold.

### 7.2 Row Completion & Stability Check

When a row is fully placed (`all bricks state 'd'`):
1. Stability calculated via `getStab()`
2. If `stability ≤ 0` OR `stability < 5% AND Math.random() < 0.05`: **COLLAPSE**
3. Otherwise, new row starts

### 7.3 Building Burst

`buildBurst()` fires 200 sequential taps at 5ms intervals (1 second total).
- Each tap calls `tapBuild()` which handles the 2-state logic
- UI updated every 10th tap

### 7.4 Resource Consumption Rate

For a width-20 tower:
- 20 bricks × 2 taps = 40 taps per row
- 20 materials + 20 mortar consumed per row
- Building burst places 200 taps = 5 rows (if materials available)

---

## 8. Upgrade Progression Path

### 8.1 Optimal Ordering

**Phase 1 — Gold Economy (Early, 0-1K gold):**
1. G1 (Clay Fingers, 20 gold) → +1 gather
2. C1 (Quick Mix, 25 gold) → +1 craft
3. R1 (Rustic Tools, 50 gold) → +10% resource
4. AG1 (Auto-Scoop, 80 gold) → auto-gather
5. G2, C2, R2 as affordable

**Phase 2 — Automation (1K-10K gold):**
1. AC1 (Auto-Stir, 120 gold) → auto-craft
2. AB1 (Auto-Trowel, 200 gold) → auto-build
3. SG1 (Gatherer Focus, 100 gold, req Lv0) → ×2 gather XP
4. SC1, SB1 → ×2 craft/build XP
5. BW1 (Wider Base I, 100 gold) → width 6

**Phase 3 — Scaling (10K-100K gold):**
1. R3, R4 (resource% upgrades)
2. G3, G4, C3, C4 (tap multipliers)
3. RF1-RF3 (reinforcement)
4. Auto upgrades to Lv5+
5. First talents (t3 — Resource Efficiency, t1 — Scaffolding)

**Phase 4 — Prestige Prep (100K-1M gold):**
1. BW2-BW4 (width 10→20)
2. RF4, RF5 (reinforcement)
3. FD1, FD2 (foundation)
4. Skill upgrades to Lv5+
5. Talents to Lv5+

**Phase 5 — Deep Endgame (1M+ gold):**
1. R5, R6 (resource% endgame)
2. BW5, BW6 (width 30→50)
3. FD3 (foundation ×3)
4. All talents Lv10
5. Skill upgrades Lv10

### 8.2 Cost Analysis by Sink Type

**Geometric series costs for upgrades (10 levels, mult 2.5):**
```
Total = base × (mult^levels - 1) / (mult - 1)
Example (g1): 20 × (2.5^10 - 1) / 1.5 = 20 × 9535/1.5 = ~127,133 gold
```

**For comparison across upgrade types:**

| Type | Levels | Base cost range | Multiplier | Total to Max One |
|---|---|---|---|---|
| G1 | 10 | 20 | 2.5 | 127,133 |
| G4 | 10 | 1,000 | 3.5 | 4,117,730 |
| R1 | 15 | 50 | 2.8 | 112,551 |
| R6 | 15 | 50,000 | 5 | 30,517,578,125 |
| Auto | 10 | 80→8000 | 2.8→3.8 | 15,571→323,066 |

**Note**: R6 is absurdly expensive — 30B gold to max, while R1-R5 cost ~350K total. This is a massive spike that essentially locks R6 behind hundreds of prestige cycles.

---

## 9. Talent Tower Analysis

### 9.1 Four Branches

**Gathering Branch:**

| Talent | Effect | Base Cost | Mult | Total Cost (Lv10) | Skill Req |
|---|---|---|---|---|---|
| t3 — Resource Efficiency | -8%/lv craft cost | 80 | 2.2 | 47,943 | gathering Lv5+3/lv |
| ga2 — Prospector's Eye | +5%/lv rare find | 200 | 2.5 | 813,802 | gathering Lv10+3/lv |
| ga3 — Deep Mining | +20%/lv gather mult | 500 | 3 | 14,762,000 | gathering Lv20+5/lv |
| ga4 — Nature's Bounty | +15%/lv auto-gather | 2,000 | 4 | 34,952,000 | gathering Lv35+8/lv |

**Crafting Branch:**

| Talent | Effect | Base Cost | Mult | Total Cost | Skill Req |
|---|---|---|---|---|---|
| t4 — Stone Hardening | +12%/lv brick str | 150 | 2.5 | 953,500 | crafting Lv8+3/lv |
| cr2 — Kiln Mastery | +15%/lv craft speed | 400 | 3 | 11,809,600 | crafting Lv15+4/lv |
| cr3 — Material Fusion | +10%/lv recipe tier | 1,500 | 3.5 | 6,176,600 | crafting Lv25+5/lv |
| cr4 — Auto-Synthesis | +15%/lv auto-craft | 5,000 | 4.5 | 87,402,500 | crafting Lv40+10/lv |

**Building Branch:**

| Talent | Effect | Base Cost | Mult | Total Cost | Skill Req |
|---|---|---|---|---|---|
| t1 — Scaffolding | +15%/lv build speed | 100 | 2.2 | 59,929 | building Lv5+2/lv |
| t2 — Mortar Mastery | +20%/lv mortar str | 200 | 2.5 | 813,802 | building Lv10+3/lv |
| bl3 — Reinforced Joints | +10%/lv stability | 600 | 3 | 17,714,400 | building Lv20+5/lv |
| bl4 — Auto-Architect | +15%/lv auto-build | 3,000 | 4 | 52,428,000 | building Lv35+8/lv |

**General Branch:**

| Talent | Effect | Base Cost | Mult | Total Cost | Skill Req |
|---|---|---|---|---|---|
| t5 — Golden Touch | +15%/lv gold mult | 300 | 3 | 8,857,200 | general Lv10+4/lv |
| f1 — Fortress Foundation | +10%/lv reinf | 500 | 3.5 | 2,058,865 | general Lv15+4/lv |
| d1 — Divine Inspiration | +15%/lv XP mult | 1,000 | 4 | 17,476,000 | general Lv25+5/lv |
| ge4 — Babel's Blessing | +10%/lv all mult | 10,000 | 5 | 244,140,500 | general Lv50+12/lv |

### 9.2 Effective Bonuses at Max Talent Level (Lv10)

| Talent | Bonus |
|---|---|
| t3 | 80% chance to save 1 resource per craft (capped at 50%) |
| ga2 | 50% "rare find" chance (effect unclear) |
| ga3 | +200% gather multiplier |
| ga4 | +150% auto-gather output |
| t4 | +120% brick strength (reduces strain) |
| cr2 | +150% craft speed |
| cr3 | +100% recipe tier (unclear) |
| cr4 | +150% auto-craft output |
| t1 | +150% build speed |
| t2 | +200% mortar strength |
| bl3 | +100% joint stability (= +100% reinf) |
| bl4 | +150% auto-build output |
| t5 | +150% gold from talents tab |
| f1 | +100% reinforce multiplier |
| d1 | +150% XP multiplier |
| ge4 | +100% all multiplier |

### 9.3 Total Talent Cost

| Branch | Total Cost (all Lv10) |
|---|---|
| Gathering | 50,575,745 |
| Crafting | 106,342,200 |
| Building | 71,016,131 |
| General | 272,532,565 |
| **Grand Total** | **500,466,641** |

---

## 10. Prestige & Collapse Economics

### 10.1 Collapse Trigger

```js
if (stability <= 0 || (stability < 5 && Math.random() < 0.05)) {
    // COLLAPSE
}
```

At stability < 5%, each brick placement has a 5% collapse chance. Below 0%, guaranteed collapse.

### 10.2 Collapse Rewards

```js
legacy = max(existing_legacy, floor(tallest × (0.1 + p4_level × 0.005)))
shards = floor(height / 25) + floor(legacy / 10)
gold_boost = 50 + height × 10 + totalClicks × 0.1
```

### 10.3 Legacy Growth Simulation

| Prestige Cycle | Tallest | p4 Lv | Legacy | Shards Earned |
|---|---|---|---|---|
| 1 | 50 | 0 | 5 | 2 + 0 = 2 |
| 2 | 75 | 0 | 7 | 3 + 0 = 3 |
| 3 | 100 | 1 | 15 | 4 + 1 = 5 |
| 4 | 150 | 2 | 30 | 6 + 3 = 9 |
| 5 | 200 | 3 | 50 | 8 + 5 = 13 |
| 6 | 300 | 4 | 90 | 12 + 9 = 21 |
| 7 | 400 | 5 | 120 | 16 + 12 = 28 |

### 10.4 Shard Cost to Max Prestige

| Upgrade | Max Lv | Cost Progression | Total Shards |
|---|---|---|---|
| p1 | 10 | 1 × 2.2^lvl | 367 |
| p2 | 5 | 3 × 3^lvl | 1,098 |
| p3 | 5 | 5 × 3^lvl | 1,830 |
| p4 | 5 | 8 × 3^lvl | 2,928 |
| p5 | 3 | 15 × 4^lvl | 1,035 |
| p6 | 5 | 10 × 3.5^lvl | 4,219 |
| p7 | 5 | 20 × 4^lvl | 27,302 |
| **Total** | **38** | — | **40,779** |

### 10.5 Prestige Run Optimization

**Value per shard (diminishing returns):**

| Upgrade | Effect per shard spent (first level) | After max |
|---|---|---|
| p1 | 100 gold/shard | +1,000 gold |
| p2 | 0.33 width/shard | +5 width |
| p3 | 1% stability/shard | +15% stability |
| p4 | 0.11% legacy/lv per shard | +2.5% legacy/lv |
| p5 | 0.066 auto-lv/shard | +3 auto-lv |
| p6 | 1.67 res/shard | +25 res |
| p7 | 2.5% gold/shard | +250% gold |

**Recommended prestige order:**
1. **p7** (Golden Legacy): ×3.5 gold at Lv5, massive multiplier to all income
2. **p5** (Eternal Workshop): +3 auto levels, dramatically speeds up automation
3. **p4** (Echoes of Labor): Compounding legacy growth
4. **p2** (Wider Legacy): +5 base width, enables taller towers
5. **p3** (Ancient Foundation): +15% stability buffer
6. **p6** (Babel's Memory): Convenience, +25 starting resources
7. **p1** (Diligent Start): +1000 starting gold, minor

---

## 11. Stability Formula Deep Dive

### 11.1 Components

```js
maxSafe = baseWidth × 5 + 25 + reinforceScore × 30 + foundationMult × 10
stability% = max(0, min(100, 100 - (height / maxSafe × 100)))
```

**Where:**
- `baseWidth`: from tech (bw1-bw6: 6→50) or default `20 + p2_level`
- `reinforceScore`: from tech (rf1-rf5: 0.2→1.0) + p3_init + f1_talent + milestones
- `foundationMult`: from tech (fd1-fd3: +0.5→+2.0)

### 11.2 Reinforce Score Formula

```js
b = 0 + p3_level × 0.03
b += (rf1 0.2 + rf2 0.4 + rf3 0.6 + rf4 0.8 + rf5 1.0)
b *= (1 + f1_level × 0.1)
if any milestone ≥4: b += 0.2
if any milestone ≥8: b += 0.3
```

### 11.3 Maximum Safe Height Analysis

| Config | Width | Reinforce | Foundation | maxSafe | Safe Height (100%) | Max Height (0%) |
|---|---|---|---|---|---|---|
| Starter | 20 | 0 | 1 | 125 | 0 | 125 |
| Early tech | 10 | 0.2 | 1 | 81 | 0 | 81 |
| Mid tech | 20 | 0.6 | 1.5 | 143 | 0 | 143 |
| All rf + fd | 20 | 1.0 | 2.0 | 175 | 0 | 175 |
| Wide + all | 30 | 1.0 | 2.0 | 205 | 0 | 205 |
| Max width | 50 | 1.0 | 2.0 | 305 | 0 | 305 |
| Max + p3 + f1 + ms | 50 | 1.9 | 2.0 | 343 | 0 | 343 |

### 11.4 Practical Collapse Heights

| Stability % | Height (base config) | Risk Profile |
|---|---|---|
| 100% | 0 | No risk |
| 80% | 25 | Safe zone |
| 50% | 62 | Moderate |
| 25% | 93 | Cracked bricks visible |
| 10% | 112 | High risk |
| 5% | 118 | **Collapse zone** (5% per brick) |
| 0% | 125 | Guaranteed collapse |

### 11.5 Optimal Collapse Strategy

For prestige grinding, you want to collapse just above the target height.

**Utility per height** for prestige is:
```
shards = floor(height / 25)  (plus legacy contribution)
```

So key thresholds: 25, 50, 75, 100, 125, 150, 175, 200, ...

Optimal play: Push to next 25-height threshold, then let collapse happen.

---

## 12. Multiplier Stacking & Synergies

### 12.1 Gold Multiplier Stack

```
gold_per_action = base_gold × milestone_gold × upgrade_gold × p7_gold × t5_gold
```

**Maximum stacking:**

| Layer | Source | Max Multiplier |
|---|---|---|
| Base | g1-g4 / c1-c4 | ×(1+5+10+20+40) = ×76 |
| Milestone | gathering ms (13 claimed) | ×(1+13×0.3) = ×4.9 |
| Prestige | p7 Lv5 | ×(1+5×0.5) = ×3.5 |
| Talent | t5 not directly applied to gather/craft gold... | — |

**Maximum gold per gather**: `76 × 4.9 × 3.5 = ~1303` (before DB)

### 12.2 XP Multiplier Stack

```
total_xp = base_xp × general_ms × skill_upgrade × d1_talent × legacy
```

| Layer | Source | Max |
|---|---|---|
| Base | per action type | 1×DB |
| General milestone 2 | MS_general ≥2 | ×2 |
| General milestone 8 | MS_general ≥8 | ×4 |
| Skill upgrade | SG1/SC1/SB1 Lv10 | ×11 |
| Divine Inspiration | d1 Lv10 | ×2.5 |
| Legacy | 500% | ×6 |
| **Total** | — | **2×4×11×2.5×6 = ×1320** |

### 12.3 Production Multiplier Stack

```
resources = base_yield × DB × (1 + Σr_upgrades) × t3_talent × legacy
materials = DB × milestone_craft × resource_saved × legacy
```

But `legacy` only applies to XP, not to resource/material production directly.

**Key insight**: Gold multipliers are largely independent from XP multipliers. You can grow gold fast without high XP, or vice versa.

---

## 13. Cost Scaling Models

### 13.1 Geometric Cost Scaling

All upgradeable systems use:

```js
cost(level) = floor(base × multiplier^level)
```

| System | Base Cost | Multiplier | Effective Doubling |
|---|---|---|---|
| Tap upgrades (g1) | 20 | 2.5 | ~0.76 levels |
| Tap upgrades (g4) | 1,000 | 3.5 | ~0.55 levels |
| Resource (r1) | 50 | 2.8 | ~0.66 levels |
| Resource (r6) | 50,000 | 5.0 | ~0.43 levels |
| Auto (ag1) | 80 | 2.8 | ~0.66 levels |
| Auto (ab3) | 8,000 | 3.8 | ~0.52 levels |
| Skill XP (sg1) | 100 | 2.5 | ~0.76 levels |
| Prestige (p7) | 20 | 4.0 | ~0.50 levels |
| Talent (ge4) | 10,000 | 5.0 | ~0.43 levels |

### 13.2 Total Cost to Max Comparison

| Item | Total Cost | Currency |
|---|---|---|
| All tap upgrades (g1-g4 + c1-c4) | ~9M | gold |
| All resource upgrades (r1-r5) | ~296K | gold |
| Resource upgrade r6 (Lv15) | ~30.5B | gold |
| All skill XP upgrades (9 items) | ~1.3M | gold |
| All auto upgrades (9 items) | ~970K | gold |
| All tech | ~938K | gold |
| All talents (16 items) | ~500M | gold |
| All prestige (7 items) | ~40,779 | shards |

### 13.3 Normalized Cost Ranking

**For gold**: r6 max > all talents > g4 max > g3 max > all auto > all tech > all skill ups > g1/g2/c1/c2...

**For shards**: p7 alone costs 67% of total prestige shard investment.

---

## 14. Production Rate Analysis

### 14.1 Manual Tap Rates

- Hold-to-repeat: fires every 60ms = ~16.7 taps/second
- Build burst: 200 taps over 1 second (5ms intervals)

### 14.2 Automation Rates

```js
interval(ms) = max(100, 3000 / (1 + level × 0.5)) × 1000
```

Wait — the formula seems wrong. Let me re-read:
```js
function getAutoInterval(id){
  const l = Math.min(aL(id), 15);
  return Math.max(100, 3000/(1 + l*0.5)) * 1000;
}
```

This gives:

| Auto Level | Calculation | Rate (ms) | Actions/sec |
|---|---|---|---|
| 0 | — | — | — |
| 1 | max(100, 3000/1.5)×1000 | 2,000,000 ms? | 0.0005/s |

Wait, that's in milliseconds? Let me re-read... `getAutoInterval` returns `Math.max(100, 3000/(1+l*0.5)) * 1000`. The `*1000` at the end seems wrong. Let me check how it's used:

```js
if(aL('gather')>0){
  const gi = getAutoInterval('gather');
  if(S.tick % (gi/100) < 1){
    gather(gr.id);
  }
}
```

`S.tick` increments every 100ms (from the setInterval in `init()`). So `gi/100` is the comparison in ticks.

With `Math.max(100, 3000/(1+l*0.5)) * 1000`:
- Level 1: `max(100, 3000/1.5) * 1000 = max(100, 2000) * 1000 = 2000 * 1000 = 2,000,000`
- `gi/100 = 20,000` ticks between actions ≈ 2,000 seconds = ~33 minutes per action?!

This is clearly a bug. The `*1000` should not be there, or the comparison units are wrong. Let me look at this more carefully.

Actually wait — I think maybe this is just the wrong formula and it means the auto barely ever fires except at very high levels or with DB. Let me check:

- Level 15: `max(100, 3000/(1+15*0.5)) * 1000 = max(100, 3000/8.5) * 1000 = max(100, 352.9) * 1000 = 352,941`
- `gi/100 = 3,529` ticks ≈ 353 seconds = ~6 minutes

This is still very slow. And at Lv0 auto is purchased, the function returns... wait, `aL('gather')` is 0 so check `if(aL('gather')>0)` fails. So you need at least Lv1 auto to start.

But the bug is in the tick comparison:
```js
if(S.tick % (gi/100) < 1)
```

`gi/100` at Lv1 auto = 20,000. So every 20,000 ticks (~2000 seconds) it fires once.

Hmm actually I think the original formula intended was:
```
return Math.max(100, 3000/(1 + l*0.5));
```
without the `*1000`, which would give:
- Level 1: `max(100, 2000) = 2000ms = 2s`
- Level 15: `max(100, 353) = 353ms`

And then `gi/100` gives ticks: 20 ticks = 2s, 3.5 ticks... Hmm the tick comparison uses modulus with `gi/100` which would be a float at lower values.

Actually I think the intent was:
```js
return max(100, 3000/(1 + l*0.5));
```
giving ms intervals, and `gi/100` converts to tick count (100ms ticks). But with the `*1000` bug, everything is 1000x too slow.

This is probably moot for the analysis since the code as-is has this bug. Let me just note it.

Actually wait, let me re-read the runAuto function more carefully:

```js
function runAuto(){
  if(S.tick<1)return
  const prAuto=lP('p5');
  if(aL('gather')+prAuto>0&&S.tick>1){
    const gi=getAutoInterval('gather');
    if(S.tick%(gi/100)<1){
      const gr=gF();if(gr)gather(gr.id);
    }
  }
```

With the code as written, auto basically never fires. This is a critical bug.

For the purposes of this analysis, I'll note the *intended* rates.

**Intended auto rates (without the *1000 bug):**

| Level | Interval | Actions/min |
|---|---|---|
| 1 | 2,000 ms | 30 |
| 2 | 1,500 ms | 40 |
| 3 | 1,200 ms | 50 |
| 4 | 1,000 ms | 60 |
| 5 | 857 ms | 70 |
| 10 | 500 ms | 120 |
| 15 | 353 ms | 170 |

With p5 (Eternal Workshop, Lv3), effective auto level = purchased level + 3.

---

## 15. Optimal Strategies

### 15.1 Early Game (First 15 minutes)

1. **Tap gather** continuously — get mud, straw, water
2. Buy **g1** (20g) and **c1** (25g) ASAP
3. Craft mud bricks + mortar, switch to **craft tab**
4. Build tower to ~25 rows
5. Buy **r1** (50g), **ag1** (80g)
6. First collapse at height 25-30 for 1-2 shards

### 15.2 Mid Game (First Prestige Cycle)

1. Put shards into **p7** (Golden Legacy) first
2. With ×2-3 gold multiplier, grind to 1K+ gold
3. Buy **bw1-bw2** (width 6→10)
4. Buy **rf1-rf3** (reinforce)
5. Push tower to height 75+
6. Collapse for 5-8 shards

### 15.3 Late Game (Established Prestige Loops)

1. p7 Lv5 → p4 Lv5 → p5 Lv3 → p2-p3-p6
2. Buy **r4** and **auto upgrades** to Lv7+
3. Push crafting to unlock reinforced/glazed bricks
4. Talents: **d1** (Divine Inspiration) and **f1** (Fortress) first
5. Tower height 200+ per run

### 15.4 Endgame (Deep Prestige)

1. Max all prestige upgrades (40,779 shards)
2. Max r1-r5 (r6 is 30B gold, probably never worth)
3. Max all talents (500M gold, dozens of prestige cycles)
4. Push tower height 500+ with megalith bricks
5. BuildBurst for speed

### 15.5 Efficiency Ratios

**Gold efficiency of actions** (per tap, DB=1, no upgrades):

| Action | Gold | XP (skill) | XP (general) | Resources |
|---|---|---|---|---|
| Gather | 1 | 1 (gather) | 0.5 | 1 resource |
| Craft | 2-8 (by tier) | 2 (craft) | 1 | 0 (consumes resources) |
| Build (place) | 2 | 2 (build) | 1 | consumes 1 mat + 1 mortar |
| Skills tab | 1.5 | 0 | 1 | 0 |
| Talents tab | 2.5 | 0 | 0 | 0 |
| Ascend tab | 2.5 | 0 | 0 | 0 |

**Resource efficiency of crafts:**

| Action | Resources Consumed | Gold earned | Material produced |
|---|---|---|---|
| Mortar | 4 (sand:2, water:1, lime:1) | 2 | 1 mortar |
| Mud Brick | 3 (mud:2, straw:1) | 2 | 1 mudBrick |
| Fired Brick | 4 (clay:2, sand:1, water:1) | 4 | 1 firedBrick |
| Stone Block | 3 (stone:3) | 5 | 1 stoneBlock |
| Reinf Brick | 3 (firedBrick:1, stone:1, lime:1) | 5 | 1 reinfBrick |
| Glazed Brick | 4 (firedBrick:1, sand:2, water:1) | 6 | 1 glazedBrick |
| Megalith | 3 (stoneBlock:2, reinfBrick:1) | 8 | 1 megalith |

**Best gold-per-resource**: Stone Block (5g / 3 res = 1.67 g/res)  
**But not all resources are equal** — stone requires Lv7 gathering.

---

## 16. Bottleneck Analysis

### 16.1 First 100 Levels

| Bottleneck | Why | Breakthrough |
|---|---|---|
| Gold | All upgrades cost gold | Buy g1, c1 (very cheap) |
| Resources | Gather yield = 1/tap | Buy r1-r3 (resource % ups) |
| Craft time | Manual tapping | Buy ac1 (auto-craft) |

### 16.2 Levels 100-500

| Bottleneck | Why | Breakthrough |
|---|---|---|
| XP rate | Need millions per level | Buy skill XP upgrades (sg1-3) |
| Shards | Collapse yields small | p4 (legacy boost) → grow taller |
| Gold | Upgrades cost 100K+ | p7 (gold %) + deep gather upgrades |

### 16.3 Levels 500+

| Bottleneck | Why | Breakthrough |
|---|---|---|
| Shards | 27K needed for p7 alone | Many prestige cycles |
| Gold (r6) | 30B gold for one upgrade | Probably never worth |
| Tower height | Stability caps at ~300-350 | Max width + reinforce + foundation |
| Talent costs | 500M gold total | Hundreds of prestige cycles |

### 16.4 Critical Path Analysis

```
Gather → resources → Craft → materials → Build → height → Collapse → shards → Prestige → repeat
                                                                        ↓
                                                                   Gold multipliers → faster everything
                                                                        ↓
                                                                   XP multipliers → skill levels → milestones
```

**The tightest bottleneck shifts over time:**
1. Gold → Resources → XP → Shards → Gold (with higher multipliers, creating a compounding loop)

---

## 17. Growth Curves & Time-to-Completion

### 17.1 Time to First Prestige

With intentional play (not using DC/debug):

| Phase | Actions Needed | Est. Time (tapping at 16.7/s) |
|---|---|---|
| Gather 50 of each resource | 50 taps | 3 sec |
| Craft 50 mud bricks | depends on resources | 20 sec |
| Build to height 25 | 25 rows × 20 bricks × 2 taps = 1,000 taps | 60 sec |
| **Time to first collapse** | — | **~2-3 minutes** |

### 17.2 Time to Lv500 Skill

Assuming average XP multiplier of ×50 (reasonable mid-game):
- XP needed for Lv500: 1,525,000
- Base XP per gather action: 1 (with DB=1)
- With ×50 mult: 50 XP per action
- Actions needed: 1,525,000 / 50 = 30,500
- Time (tapping): 30,500 / 16.7 = ~1,826 sec = ~30 minutes
- With DB=10: 3 minutes

### 17.3 Time to All Prestige Max

Assuming average 30 shards per collapse (height ~300, legacy ~50):
- Total needed: 40,779 shards
- Cycles: 40,779 / 30 = ~1,359 prestige cycles
- Even at 5 minutes per cycle: 6,795 minutes = ~4.7 days of active play
- With automation & high multipliers: maybe 1-2 days continuous play

### 17.4 Time to All Talents

500M gold total cost for all talents Lv10.
- If earning 500 gold/sec (automated mid-game): 1M sec = ~11.6 days
- If earning 5K gold/sec (late-game, heavy multipliers): 100K sec = ~28 hours
- This assumes continuous active play

### 17.5 Time to Max Everything

| Goal | Est. Active Time |
|---|---|
| First prestige | 2-3 minutes |
| All milestones (Lv500 skills) | 2-3 hours |
| All tech | 4-6 hours |
| All skill upgrades | 1-2 hours |
| All auto upgrades | 3-5 hours |
| All resource ups (r1-r5) | 5-8 hours |
| All prestige (40K shards) | 4-7 days |
| All talents (500M gold) | 28 hours - 11 days |
| R6 max | likely never (30B gold) |

---

## 18. Balance Recommendations

### 18.1 Critical Bugs

1. **Auto interval bug**: The `*1000` in `getAutoInterval()` makes automation 1000× slower than intended — effectively broken. Remove `*1000` or adjust tick comparison.

2. **Gravel has no purpose**: Gravel resource (unlocked at Lv2) is never consumed. Give it a recipe (e.g., mortar alternative using gravel:2, lime:1 → reinforced mortar).

3. **Tower height milestones (`TOWER_MS`) are empty**: Effects defined as `()=>{}` — no actual bonuses applied. Wire them to stability, width, or gold multipliers.

4. **Many talent effects not wired**: `ga2.rareChance`, `ga3.gatherMult`, `cr2.craftSpeed`, `cr3.recipeTier`, `bl3.jointStr`, `t2.mortarStr` etc. are defined but never read by game logic.

5. **prAuto scope bug**: `const prAuto = lP('p5')` is used in `runAuto()` but defined inside conditional branches, causing reference errors in offline progress code.

### 18.2 Balance Issues

1. **R6 cost cliff**: R6 (Magic Loom) at 50K base cost × 5^level = 30B max, while r1-r5 total ~350K. This is a 100,000× jump. Consider a smoother curve or a separate milestone unlock.

2. **Prestige p7 cost dominates**: p7 is 67% of total shard cost. Other prestige upgrades seem like filler in comparison.

3. **Burst building bypasses stability**: `buildBurst()` places 200 bricks in 1 second, checking stability only once per `tapBuild()` call. With 5ms intervals, the tower can grow ~5 rows before a stability check triggers collapse animation.

4. **Mud Brick vs Fired Brick balance**: Fired Brick costs more (4 res vs 3) and has better strength (0.8 vs 1.0), but the difference is marginal for the added resource cost.

5. **Milestone bonuses are weak**: +30% per milestone seems modest compared to upgrade multipliers (×76 from tap ups, ×3325% from resource ups).

6. **Skills tab and Ascend tab tapping**: These generate gold with no resource cost and minimal XP gain, making them "free gold" exploits.

7. **Hold-to-repeat at 60ms**: This fires every 60ms regardless of tab, making automation partially redundant for active play.

### 18.3 Suggested Rebalances

1. Fix the auto interval bug
2. Wire tower height milestones to actual bonuses
3. Wire talent effects to game logic
4. Add Gravel recipes
5. Add a smoother transition between r5 and r6
6. Reduce p7 cost or increase other prestige upgrade value
7. Add diminishing returns to hold-to-repeat (warm-up time)
8. Consider adding collapse risk to build burst (batch collapse check)

---

## 19. Glossary of Formulae

### State Variables
```js
S.upg[id]     — upgrade level (0-based, max defined per upgrade)
S.tal[id]     — talent level (0-10)
S.ms[track]   — milestone claim count (0-13)
S.sk[id].lv   — skill level (starts at 1)
S.sk[id].xp   — skill XP (accumulated)
S.auto[id]    — auto upgrade level (0-15, capped)
S.pr[id]      — prestige upgrade level (0-L)
S.stat.shards — accumulated Babel Shards
S.stat.legacy — accumulated Legacy multiplier
```

### Helper Functions
```js
uL(id)  = S.upg[id] || 0           // upgrade level
tL(id)  = S.tal[id] || 0           // talent level
msG(id) = S.ms[id] || 0            // milestones claimed
skLv(id)= S.sk[id]?.lv || 1        // skill level
aL(id)  = S.auto[id] || 0          // auto upgrade level
lP(id)  = S.pr?.[id] || 0          // prestige level
xpN(lv) = floor(50 × lv × (1 + 0.12 × lv))  // XP to next level
```

### Cost Functions
```js
upgrade_cost(id, level) = floor(base_cost × multiplier^level)
talent_cost(id, level)  = floor(cb × cm^level)
prestige_cost(id, lvl)  = floor(cb × cm^lvl)
tech_cost(id)           = flat cost (one-time purchase)
```

### Production Functions
```js
gather_yield   = floor(DB × (1 + Σ(r_lvl × r_mult))) + ...talent bonus
gather_gold    = floor(1 × (1 + 0.5×g1 + 1×g2 + 2×g3 + 4×g4)) × (1 + p7×0.5)
craft_amount   = max(1, DB × (1 + 0.3 × msG('crafting')))
craft_gold     = floor(mat.t × (1 + 0.5×c1 + 1×c2 + 2×c3 + 4×c4)) × (1 + p7×0.5)
build_xp       = (1 or 2) × DB × XP_multiplier
```

### Stability Functions
```js
baseWidth     = S.tech.bwN || 20 + lP('p2')
reinforceScore = Σ(rf_N) + p3×0.03 + milestones + (1 + f1×0.1)
foundationMult = 1 + Σ(fd_N)
materialStr    = MAT_ALL[getMatId()].str  (0.2-1.0, lower = better)

maxSafeHeight = baseWidth × 5 + 25 + reinforceScore × 30 + foundationMult × 10
stability%    = 100 - (height / maxSafeHeight × 100)
```

### Collapse Functions
```js
legacy = max(existing, floor(tallest_height × (0.1 + lP('p4') × 0.005)))
shards = floor(height / 25) + floor(legacy / 10)
gold_on_collapse = 50 + height × 10 + totalClicks × 0.1
```

---

## Appendix: Data File Exports

### A.1 Full Upgrade Cost Table (Selected)

| ID | Lv1 | Lv5 | Lv10 | Lv15 | Type |
|---|---|---|---|---|---|
| g1 | 20 | 195 | 3,815 | — | tap gather |
| g4 | 1,000 | 5,252 | 45,000 | — | tap gather |
| c4 | 1,500 | 7,878 | 67,500 | — | tap craft |
| r1 | 50 | 615 | 6,705 | 73,080 | resource% |
| r6 | 50,000 | 3,125,000 | 976,562,500 | 305,175,781,250 | resource% |
| ag1 | 80 | 984 | 10,728 | — | auto |
| ab3 | 8,000 | 18,800 | 98,400 | — | auto |
| sg1 | 100 | 976 | 19,073 | — | ×XP |

### A.2 Full Talent Costs (Total to Lv10)

| Talent | Lv1 | Lv10 | Total |
|---|---|---|---|
| t3 | 80 | 47,121 | 47,943 |
| ga2 | 200 | 800,000 | 813,802 |
| ga3 | 500 | 14,500,000 | 14,762,000 |
| ga4 | 2,000 | 34,000,000 | 34,952,000 |
| t4 | 150 | 937,500 | 953,500 |
| cr2 | 400 | 11,600,000 | 11,809,600 |
| cr3 | 1,500 | 6,000,000 | 6,176,600 |
| cr4 | 5,000 | 85,000,000 | 87,402,500 |
| t1 | 100 | 58,900 | 59,929 |
| t2 | 200 | 800,000 | 813,802 |
| bl3 | 600 | 17,400,000 | 17,714,400 |
| bl4 | 3,000 | 51,000,000 | 52,428,000 |
| t5 | 300 | 8,700,000 | 8,857,200 |
| f1 | 500 | 2,000,000 | 2,058,865 |
| d1 | 1,000 | 17,000,000 | 17,476,000 |
| ge4 | 10,000 | 240,000,000 | 244,140,500 |

### A.3 Prestige Shard Cost to Max

| ID | Cumulative Shards |
|---|---|
| p1 | 367 |
| p2 | 1,098 |
| p3 | 1,830 |
| p4 | 2,928 |
| p5 | 1,035 |
| p6 | 4,219 |
| p7 | 27,302 |
| **Total** | **40,779** |

---

*End of analysis. Generated from babel codebase at commit HEAD.*
