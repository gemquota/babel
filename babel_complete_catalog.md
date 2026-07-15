# Babel — Complete Game Systems Catalog

> **Exhaustive reference of every mechanic, upgrade, resource, material, talent, tech, milestone, prestige bonus, tracked stat, and state variable in the game.**
>
> Source: `index.html` — single-file HTML/CSS/JS incremental game
> Last updated with all fixes from v2 applied

---

## Table of Contents

1. [Currency Systems](#1-currency-systems)
2. [Resources (Gatherable)](#2-resources-gatherable)
3. [Materials (Craftable)](#3-materials-craftable)
4. [Tap Upgrades — Gather Gold (G1-G6)](#4-tap-upgrades--gather-gold-g1-g6)
5. [Tap Upgrades — Craft Gold (C1-C6)](#5-tap-upgrades--craft-gold-c1-c6)
5b. [Build Gold Upgrades (B1-B4)](#5b-build-gold-upgrades-b1-b4)
6. [Resource % Upgrades (R1-R12)](#6-resource--upgrades-r1-r12)
7. [Auto Upgrades — Gather (AG1-AG5)](#7-auto-upgrades--gather-ag1-ag5)
8. [Auto Upgrades — Craft (AC1-AC5)](#8-auto-upgrades--craft-ac1-ac5)
9. [Auto Upgrades — Build (AB1-AB5)](#9-auto-upgrades--build-ab1-ab5)
9b. [Auto Upgrades — Skill (AM1-AM3)](#9b-auto-upgrades--meditation-am1-am3)
10. [Skill XP Upgrades (SG1-SG5 / SC1-SC5 / SB1-SB5 / SM1-SM5)](#10-skill-xp-upgrades-sg1-sg5--sc1-sc5--sb1-sb5--sm1-sm5)
11. [Burst Engine Upgrades (BP / BS / BC / BCD / BCH / BW / BA / BF / BR / BB)](#11-burst-engine-upgrades)
12. [Tower Tech — Width (BW1-BW12)](#12-tower-tech--width-bw1-bw12)
13. [Tower Tech — Reinforce (RF1-RF10)](#13-tower-tech--reinforce-rf1-rf10)
14. [Tower Tech — Foundation (FD1-FD8)](#14-tower-tech--foundation-fd1-fd8)
14b. [Tower Tech — Buttress (BR1-BR4)](#14b-tower-tech--buttress-br1-br4)
14c. [Tower Tech — Pillar (PI1-PI4)](#14c-tower-tech--pillar-support-pi1-pi4)
14d. [Tower Tech — Dampener (DM1-DM3)](#14d-tower-tech--dampener-dm1-dm3)
15. [Tower Height Milestones](#15-tower-height-milestones)
16. [Skill Milestones — Gathering](#16-skill-milestones--gathering)
17. [Skill Milestones — Crafting](#17-skill-milestones--crafting)
18. [Skill Milestones — Building](#18-skill-milestones--building)
19. [Skill Milestones — General](#19-skill-milestones--general)
19b. [Skill Milestones — Mastery](#19b-skill-milestones--mastery)
20. [Talents — Gathering Branch](#20-talents--gathering-branch)
21. [Talents — Crafting Branch](#21-talents--crafting-branch)
22. [Talents — Building Branch](#22-talents--building-branch)
23. [Talents — General Branch](#23-talents--general-branch)
23b. [Talents — Mastery Branch](#23b-talents--mastery-branch)
24. [Prestige Upgrades (P1-P10)](#24-prestige-upgrades-p1-p10)
25. [Prestige Collapse Rewards](#25-prestige-collapse-rewards)
26. [Color Constants & Visual Theme](#26-color-constants--visual-theme)
27. [State Object Structure (S)](#27-state-object-structure-s)
28. [Tracked Statistics](#28-tracked-statistics)
29. [Helper Functions](#29-helper-functions)
30. [Tower Stability Formula](#30-tower-stability-formula)
31. [XP & Leveling Formulas](#31-xp--leveling-formulas)
32. [Gold Generation Formulas](#32-gold-generation-formulas)
33. [Automation Interval Formula](#33-automation-interval-formulas)
34. [Cost Scaling Formulas](#34-cost-scaling-formulas)
35. [Burst Engine Formulas](#35-burst-engine-formulas)
36. [Input Methods & UI Bindings](#36-input-methods--ui-bindings)
37. [Debug Mode Controls](#37-debug-mode-controls)
38. [Save System](#38-save-system)
39. [Tab Structure](#39-tab-structure)
40. [Animation & Visual Systems](#40-animation--visual-systems)

---

## 1. Currency Systems

| Currency | Symbol | Variable | Earned By | Spent On |
|---|---|---|---|---|
| Gold | 🪙 | `S.stat.gold` | All actions, all tabs | Upgrades, tech, talents, burst costs |
| Resources | R (🟤) | `S.res[id]` | Gather tab | Crafting recipes |
| Materials | 🧱 | `S.mat[id]` | Craft tab | Building tower bricks |
| Babel Shards | 💎 | `S.stat.shards` | Tower collapse | Prestige upgrades |
| Legacy | % | `S.stat.legacy` | Tower collapse | Passive XP multiplier (1%/point) |

---

## 2. Resources (Gatherable)

Array: `RES_ALL` — unlocked by gathering skill level

| ID | Name | Icon | Base Yield | Unlock (Gather Lv) | Used In |
|---|---|---|---|---|---|
| mud | Mud | 🟤 | 1 | 0 | Mud Brick (mud:2, straw:1) |
| water | Water | 💧 | 1 | 0 | Mortar, Fired Brick, Glazed Brick |
| straw | Straw | 🌾 | 1 | 0 | Mud Brick (mud:2, straw:1) |
| gravel | Gravel | 🪨 | 1 | 2 | Mortar (sand:1, gravel:1, water:1, lime:1) |
| sand | Sand | 🏖️ | 1 | 3 | Mortar, Fired Brick, Glazed Brick |
| clay | Clay | 🧱 | 1 | 4 | Fired Brick (clay:2, sand:1, water:1) |
| lime | Lime | 🪨 | 1 | 5 | Mortar, Reinforced Brick |
| stone | Stone | ⛰️ | 1 | 7 | Stone Block (stone:3), Reinforced Brick |
| ruby | Ruby | 🔴 | 1 | 10 | Gemstone crafting |
| sapphire | Sapphire | 🔵 | 1 | 13 | Gemstone crafting |
| emerald | Emerald | 🟢 | 1 | 16 | Gemstone crafting |
| diamond | Diamond | 💎 | 1 | 20 | Gemstone Brick |
| ash | Ash | 🖤 | 1 | 6 | Ash Brick |
| charcoal | Charcoal | 🪵 | 1 | 8 | Charcoal Brick, Iron Brick, Steel Beam |
| sulfur | Sulfur | 🟡 | 1 | 9 | Sulfur Brick |
| mercury | Mercury | 🪩 | 1 | 11 | Advanced alloys |
| iron_ore | Iron Ore | ⛏️ | 1 | 12 | Iron Brick |
| titanium_ore | Titanium | ⚪ | 1 | 15 | Titanium Plate |
| mithril_ore | Mithril | 🔮 | 1 | 18 | Mithril Block |
| crystal_shard | Crystal | 💠 | 1 | 22 | Crystal Block |
| void_essence | Void Essence | 🟣 | 1 | 25 | Void Stone |
| aether_dust | Aether | ✨ | 1 | 28 | Aether Brick |
| dragon_scale | Dragon Scale | 🐉 | 1 | 32 | Dragon Block |
| star_shard | Star Shard | ⭐ | 1 | 36 | Star Brick |

---

## 3. Materials (Craftable)

Array: `MAT_ALL` — unlocked by crafting skill level

| ID | Name | Icon | Tier (t) | Strength (str) | Unlock (Craft Lv) | Recipe |
|---|---|---|---|---|---|---|
| mortar | Mortar | 🧴 | 2 | 0 (decorative) | 0 | sand:1 + gravel:1 + water:1 + lime:1 |
| mudBrick | Mud Brick | 🧱 | 2 | 1.0 | 0 | mud:2 + straw:1 |
| firedBrick | Fired Brick | 🔥 | 4 | 0.7 | 3 | clay:2 + sand:1 + water:1 |
| stoneBlock | Stone Block | 🗿 | 5 | 0.6 | 6 | stone:3 |
| reinfBrick | Reinf. Brick | ⚔️ | 5 | 0.4 | 8 | firedBrick:1 + stone:1 + lime:1 |
| glazedBrick | Glazed Brick | ✨ | 6 | 0.3 | 12 | firedBrick:1 + sand:2 + water:1 |
| megalith | Megalith | 🏛️ | 8 | 0.2 | 18 | stoneBlock:2 + reinfBrick:1 |
| concrete | Concrete Block | 🧊 | 5 | 0.5 | 10 | gravel:3 + sand:1 + water:1 |
| marble | Marble Block | 🤍 | 6 | 0.35 | 14 | stone:4 |
| granite | Granite Block | 🪨 | 6 | 0.33 | 16 | stone:3 + gravel:2 |
| obsidian | Obsidian Brick | 🖤 | 7 | 0.25 | 20 | stone:2 + firedBrick:1 |
| onyx | Onyx Brick | ⚫ | 8 | 0.18 | 22 | glazedBrick:1 + obsidian:1 |
| gemBrick | Gemstone Brick | 💠 | 10 | 0.10 | 25 | megalith:1 + diamond:1 |
| ashBrick | Ash Brick | 🖤 | 3 | 0.90 | 6 | ash:3 + water:1 |
| charcoalBrick | Charcoal Brick | 🪨 | 3 | 0.85 | 7 | charcoal:2 + clay:1 |
| sulfurBrick | Sulfur Brick | 🟨 | 5 | 0.55 | 9 | sulfur:2 + firedBrick:1 |
| ironBrick | Iron Brick | ⚙️ | 6 | 0.40 | 11 | iron_ore:4 + charcoal:2 |
| steelBeam | Steel Beam | 🏗️ | 7 | 0.30 | 13 | ironBrick:2 + charcoal:1 |
| titaniumPlate | Titanium Plate | 🛡️ | 7 | 0.28 | 15 | titanium_ore:4 + steelBeam:1 |
| composite | Composite Block | 🧬 | 9 | 0.22 | 21 | megalith:1 + titaniumPlate:1 + obsidian:1 |
| mithrilBlock | Mithril Block | 🔷 | 8 | 0.15 | 19 | mithril_ore:3 + steelBeam:1 |
| crystalBlock | Crystal Block | 💎 | 9 | 0.12 | 23 | crystal_shard:4 + mithrilBlock:1 |
| voidStone | Void Stone | ⬛ | 10 | 0.08 | 27 | void_essence:3 + crystalBlock:1 |
| aetherBrick | Aether Brick | ☁️ | 11 | 0.05 | 30 | aether_dust:4 + voidStone:1 |
| dragonBlock | Dragon Block | 🐉 | 12 | 0.03 | 34 | dragon_scale:3 + aetherBrick:1 |
| starBrick | Star Brick | 🌟 | 14 | 0.01 | 38 | star_shard:3 + dragonBlock:1 |

Note: Lower `str` = stronger brick (less strain on tower stability). (less strain on tower stability).

---

## 4. Tap Upgrades — Gather Gold (G1-G4)

Array: `UPG_G` — all use `sk:'gather'`

| ID | Name | Effect | Base Cost | Cost Mult | Max Lv | Per Level Value |
|---|---|---|---|---|---|---|
| g1 | Clay Fingers | +gather gold per tap | 20 🪙 | 2.5 | 10 | +0.5 gold multiplier |
| g2 | Sharp Eye | +gather gold per tap | 80 🪙 | 3.0 | 10 | +1.0 gold multiplier |
| g3 | Iron Will | +gather gold per tap | 300 🪙 | 3.2 | 10 | +2.0 gold multiplier |
| g4 | Stone Hands | +gather gold per tap | 1,000 🪙 | 3.5 | 10 | +4.0 gold multiplier |
| g5 | Diamond Touch | +gather gold per tap | 5,000 🪙 | 4.0 | 10 | +8.0 gold multiplier |
| g6 | Midas Touch | +gather gold per tap | 25,000 🪙 | 5.0 | 10 | +16.0 gold multiplier |

**Formula**: `gatherGoldMult = 1 + 0.5×g1 + 1.0×g2 + 2.0×g3 + 4.0×g4 + 8.0×g5 + 16.0×g6`

---

## 5. Tap Upgrades — Craft Gold (C1-C4)

Array: `UPG_G` — all use `sk:'craft'`

| ID | Name | Effect | Base Cost | Cost Mult | Max Lv | Per Level Value |
|---|---|---|---|---|---|---|
| c1 | Quick Mix | +craft gold per tap | 25 🪙 | 2.5 | 10 | +0.5 gold × tier |
| c2 | Efficient Kiln | +craft gold per tap | 100 🪙 | 3.0 | 10 | +1.0 gold × tier |
| c3 | Assembly Line | +craft gold per tap | 400 🪙 | 3.2 | 10 | +2.0 gold × tier |
| c4 | Auto-Forge | +craft gold per tap | 1,500 🪙 | 3.5 | 10 | +4.0 gold × tier |
| c5 | Quantum Kiln | +craft gold per tap | 8,000 🪙 | 4.0 | 10 | +8.0 gold × tier |
| c6 | Cosmic Forge | +craft gold per tap | 40,000 🪙 | 5.0 | 10 | +16.0 gold × tier |

**Formula**: `craftGoldMult = 1 + 0.5×c1 + 1.0×c2 + 2.0×c3 + 4.0×c4 + 8.0×c5 + 16.0×c6`

---

### 5b. Build Gold Upgrades (B1-B4)

Array: `UPG_G` - `sk:'build'`

| ID | Name | Effect | Base Cost | Cost Mult | Max Lv |
|---|---|---|---|---|---|
| b1 | Steady Hand | +1 build gold | 50 🪙 | 2.5 | 10 |
| b2 | Precision Trowel | +2 build gold | 200 🪙 | 3.0 | 10 |
| b3 | Master Mason | +4 build gold | 800 🪙 | 3.2 | 10 |
| b4 | Grand Architect | +8 build gold | 3,000 🪙 | 3.5 | 10 |

---

## 6. Resource % Upgrades (R1-R12)

Array: `UPG_R` — all use `sk:'gather'`

| ID | Name | Effect | Base Cost | Cost Mult | Max Lv | Per Level Value |
|---|---|---|---|---|---|---|
| r1 | Rustic Tools | +10% resource gain | 50 🪙 | 2.8 | 15 | +0.10 |
| r2 | Ox Cart | +15% resource gain | 200 🪙 | 3.2 | 15 | +0.15 |
| r3 | Water Wheel | +20% resource gain | 800 🪙 | 3.5 | 15 | +0.20 |
| r4 | Crane | +30% resource gain | 3,000 🪙 | 4.0 | 15 | +0.30 |
| r5 | Steam Engine | +50% resource gain | 12,000 🪙 | 4.5 | 15 | +0.50 |
| r6 | Magic Loom | +100% resource gain | 5,000 🪙 | 3.5 | 15 | +1.00 |
| r7 | Alchemy Lab | +200% resource gain | 30,000 🪙 | 4.0 | 15 | +2.00 |
| r8 | Dowsing Rod | +300% resource gain | 100,000 🪙 | 4.5 | 15 | +3.00 |
| r9 | Elemental Well | +500% resource gain | 500,000 🪙 | 5.0 | 15 | +5.00 |
| r10 | Dimensional Rift | +1000% resource gain | 2,000,000 🪙 | 5.5 | 15 | +10.00 |
| r11 | Cosmic Well | +2000% resource gain | 10,000,000 🪙 | 6.0 | 15 | +20.00 |
| r12 | Singularity | +5000% resource gain | 50,000,000 🪙 | 6.5 | 15 | +50.00 |

**Formula**: `resourceMult = 1 + Σ(r_lv × r_value)`

---

## 7. Auto Upgrades — Gather (AG1-AG3)

Array: `UPG_A` — `sk:'gather'`

| ID | Name | Effect | Base Cost | Cost Mult | Max Lv |
|---|---|---|---|---|---|
| ag1 | Auto-Scoop | Auto-gather | 80 🪙 | 2.8 | 10 |
| ag2 | Auto-Windmill | Faster auto-gather II | 500 🪙 | 3.2 | 10 |
| ag3 | Auto-Earth Mover | Faster auto-gather III | 3,000 🪙 | 3.8 | 10 |

Each upgrade adds +1 effective auto-gather level. Combined max effective: Lv15.

---

## 8. Auto Upgrades — Craft (AC1-AC3)

Array: `UPG_A` — `sk:'craft'`

| ID | Name | Effect | Base Cost | Cost Mult | Max Lv |
|---|---|---|---|---|---|
| ac1 | Auto-Stir | Auto-craft | 120 🪙 | 2.8 | 10 |
| ac2 | Auto-Press | Faster auto-craft II | 800 🪙 | 3.2 | 10 |
| ac3 | Auto-Factory | Faster auto-craft III | 5,000 🪙 | 3.8 | 10 |

Each upgrade adds +1 effective auto-craft level. Combined max effective: Lv15.

---

## 9. Auto Upgrades — Build (AB1-AB3)

Array: `UPG_A` — `sk:'build'`

| ID | Name | Effect | Base Cost | Cost Mult | Max Lv |
|---|---|---|---|---|---|
| ab1 | Auto-Trowel | Auto-build | 200 🪙 | 2.8 | 10 |
| ab2 | Auto-Crane | Faster auto-build II | 1,200 🪙 | 3.2 | 10 |
| ab3 | Auto-Gigalith | Faster auto-build III | 8,000 🪙 | 3.8 | 10 |

Each upgrade adds +1 effective auto-build level. Combined max effective: Lv15.

---

## 10. Skill XP Upgrades

Array: `UPG_S`

### Gathering XP (Gatherer tree)

| ID | Name | Effect | Base Cost | Cost Mult | Max Lv | Skill Req |
|---|---|---|---|---|---|---|
| sg1 | Gatherer Focus | ×2 gather rate | 100 🪙 | 2.5 | 10 | Gathering Lv0 |
| sg2 | Gatherer Mastery | ×3 gather rate | 2,000 🪙 | 4 | 10 | Gathering Lv5 |
| sg3 | Gatherer Supremacy | ×5 gather rate | 20,000 🪙 | 5 | 10 | Gathering Lv10 |

### Crafting XP (Crafter tree)

| ID | Name | Effect | Base Cost | Cost Mult | Max Lv | Skill Req |
|---|---|---|---|---|---|---|
| sc1 | Crafter Focus | ×2 craft rate | 100 🪙 | 2.5 | 10 | Crafting Lv0 |
| sc2 | Crafter Mastery | ×3 craft rate | 2,000 🪙 | 4 | 10 | Crafting Lv5 |
| sc3 | Crafter Supremacy | ×5 craft rate | 20,000 🪙 | 5 | 10 | Crafting Lv10 |

### Building XP (Builder tree)

| ID | Name | Effect | Base Cost | Cost Mult | Max Lv | Skill Req |
|---|---|---|---|---|---|---|
| sb1 | Builder Focus | ×2 build rate | 100 🪙 | 2.5 | 10 | Building Lv0 |
| sb2 | Builder Mastery | ×3 build rate | 2,000 🪙 | 4 | 10 | Building Lv5 |
| sb3 | Builder Supremacy | ×5 build rate | 20,000 🪙 | 5 | 10 | Building Lv10 |

**Formula**: `skillXPMult = 1 + upgrade_lv` (e.g., sg1 Lv10 = ×11 gather XP)

---

## 11. Burst Engine Upgrades

Array: `BURST_UPG`

| ID | Name | Icon | Effect | Base Cost | Cost Mult | Max Lv | Progression |
|---|---|---|---|---|---|---|---|
| bp | Crane Power | 🏗️ | +20 taps/burst | 200 🪙 | 2.5 | 10 | `20 + lv×20` (max 220) |
| bs | Pulley Speed | ⚡ | -5ms/action | 400 🪙 | 2.8 | 8 | `max(10, 50-lv×5)` (min 10ms) |
| bc | Bulk Order | 💰 | -2🪙 cost | 300 🪙 | 2.5 | 10 | `max(0, 20-lv×2)` (frees at Lv10) |
| bcd | Crew Cooldown | ⏳ | -2s cooldown | 500 🪙 | 3 | 9 | `max(2, 20-lv×2)` (min 2s) |
| bch | Reserve Crew | 👥 | +1 max charge | 1,000 🪙 | 3.5 | 5 | `1 + lv` (max 6 charges) |

---

## 12. Tower Tech — Width (BW1-BW6)

Array: `TECH` — type `'w'`

| ID | Name | Width | Cost 🪙 | Notes |
|---|---|---|---|---|
| bw1 | Wider Base I | 6 | 100 | Minimum width tech |
| bw2 | Wider Base II | 10 | 500 | |
| bw3 | Wider Base III | 15 | 2,500 | |
| bw4 | Wider Base IV | 20 | 15,000 | |
| bw5 | Wider Base V | 30 | 100,000 | |
| bw6 | Stress Test | 50 | 500,000 | stress:1 (marked as risky) |
| bw7 | Wider Base VII | 100 | 2,000,000 | |
| bw8 | Wider Base VIII | 200 | 5,000,000 | |
| bw9 | Wider Base IX | 500 | 20,000,000 | stress:1 |
| bw10 | Wider Base X | 100 | 1,000,000 | |
| bw11 | Wider Base XI | 150 | 5,000,000 | |
| bw12 | Wider Base XII | 250 | 20,000,000 | stress:1 |

Base width without tech: `20 + lP('p2')` (prestige can add up to +5).

---

## 13. Tower Tech — Reinforce (RF1-RF5)

Array: `TECH` — type `'r'`

| ID | Name | Stability Bonus | Cost 🪙 |
|---|---|---|---|
| rf1 | Reinforce I | +0.20 | 200 |
| rf2 | Reinforce II | +0.40 | 1,000 |
| rf3 | Reinforce III | +0.60 | 5,000 |
| rf4 | Reinforce IV | +0.80 | 30,000 |
| rf5 | Reinforce V | +1.00 | 200,000 |
| rf6 | Reinforce VI | +1.50 | 1,000,000 |
| rf7 | Reinforce VII | +2.00 | 5,000,000 |
| rf8 | Reinforce VIII | +3.00 | 20,000,000 |
| rf9 | Reinforce IX | +4.00 | 10,000,000 |
| rf10 | Reinforce X | +5.00 | 50,000,000 |

Reinforce adds to `maxSafe` via +30 per 0.2 reinforce.

---

## 14. Tower Tech — Foundation (FD1-FD3)

Array: `TECH` — type `'f'`

| ID | Name | Strength Mult | Cost 🪙 |
|---|---|---|---|
| fd1 | Foundation I | +0.5 (×1.5) | 1,000 |
| fd2 | Foundation II | +1.0 (×2.0) | 8,000 |
| fd3 | Foundation III | +2.0 (×3.0) | 60,000 |
| fd4 | Foundation IV | +3.0 (×4.0) | 500,000 |
| fd5 | Foundation V | +6.0 (×7.0) | 2,000,000 |
| fd6 | Foundation VI | +13.0 (×14.0) | 10,000,000 |
| fd7 | Foundation VII | +19.0 (×20.0) | 50,000,000 |
| fd8 | Foundation VIII | +49.0 (×50.0) | 200,000,000 |

Foundation multiplies the foundation factor in maxSafe: `foundationMult = 1 + Σ(fd_values)`.

---

### 14b. Tower Tech - Buttress (BR1-BR4)

Array: `TECH` - type `'x'`

| ID | Name | Stability Threshold | Cost 🪙 |
|---|---|---|---|
| br1 | Buttress I | +0.20 | 300,000 |
| br2 | Buttress II | +0.30 | 1,500,000 |
| br3 | Buttress III | +0.50 | 8,000,000 |
| br4 | Buttress IV | +0.80 | 40,000,000 |

### 14c. Tower Tech - Pillar Support (PI1-PI4)

Array: `TECH` - type `'p'`

| ID | Name | MaxSafe Bonus | Cost 🪙 |
|---|---|---|---|
| pi1 | Pillar Support I | +5 | 500,000 |
| pi2 | Pillar Support II | +10 | 3,000,000 |
| pi3 | Pillar Support III | +20 | 15,000,000 |
| pi4 | Pillar Support IV | +40 | 75,000,000 |

### 14d. Tower Tech - Dampener (DM1-DM3)

Array: `TECH` - type `'d'`

| ID | Name | Collapse Risk Reduction | Cost 🪙 |
|---|---|---|---|
| dm1 | Dampener I | -15% | 2,000,000 |
| dm2 | Dampener II | -25% | 15,000,000 |
| dm3 | Dampener III | -40% | 100,000,000 |

---

## 15. Tower Height Milestones

Array: `TOWER_MS` — one-time permanent bonuses unlocked by reaching heights. Tracked in `S.tower.tm` (bitmask).

| # | Height | Name/Bonus | Type | Effect on Gameplay |
|---|---|---|---|---|
| 0 | 1 | Tutorial | none | Just a notification |
| 1 | 10 | +10% tower width | width | `baseWidth ×= 1.1` each claim |
| 2 | 25 | +5% stability | stability | `stability += 5` per claim |
| 3 | 50 | Gold reward ×2 | gold | `buildGold ×= 2` |
| 4 | 100 | Auto-repair cracks | repair | Collapse risk ÷3 in hazard zone |
| 5 | 200 | Foundation ×2 | foundation | `foundationMult ×= 2` per claim |
| 6 | 500 | Legacy amplifier | legacy | Small legacy gain on brick place |

---

## 16. Skill Milestones — Gathering

Array: `MS.gathering` — 13 tiers. Tracked in `S.ms.gathering` (count claimed).

| # | Lv Req | Title | Effect |
|---|---|---|---|
| 0 | 5 | Gatherer Apprentice | +50% gold per gather (per milestone claimed) |
| 1 | 10 | Prospector | +50% gold per gather (stacking) |
| 2 | 25 | Excavator | +50% gold per gather (stacking) |
| 3 | 50 | Quarry Master | +50% gold per gather + +0.2 reinforce |
| 4 | 75 | Mountain Mover | +50% gold per gather (stacking) |
| 5 | 100 | Earth Shaper | +50% gold per gather (stacking) |
| 6 | 125 | Terrain Forger | +50% gold per gather (stacking) |
| 7 | 150 | Resource Sage | +50% gold per gather (stacking) |
| 8 | 200 | Land Cleaver | +50% gold per gather + +0.3 reinforce |
| 9 | 250 | Mine Lord | +50% gold per gather (stacking) |
| 10 | 300 | World Harvester | +50% gold per gather (stacking) |
| 11 | 400 | Elemental Collector | +50% gold per gather (stacking) |
| 12 | 500 | Gathering God | +50% gold per gather (stacking) |

**Total bonus at 13/13**: gold mult `×(1 + 13×0.5) = ×7.5`, reinforce `+0.5`

---

## 17. Skill Milestones — Crafting

Array: `MS.crafting` — 13 tiers. Tracked in `S.ms.crafting`.

| # | Lv Req | Title | Effect |
|---|---|---|---|
| 0 | 5 | Crafter Apprentice | +50% craft amount (per milestone claimed) |
| 1 | 10 | Artisan | +50% craft amount (stacking) |
| 2 | 25 | Workshop Master | +50% craft amount (stacking) |
| 3 | 50 | Factory Owner | +50% craft amount (stacking) |
| 4 | 75 | Industrialist | +50% craft amount (stacking) |
| 5 | 100 | Innovator | +50% craft amount (stacking) |
| 6 | 125 | Master Artisan | +50% craft amount (stacking) |
| 7 | 150 | Manufacturing Sage | +50% craft amount (stacking) |
| 8 | 200 | Grand Builder | +50% craft amount (stacking) |
| 9 | 250 | Assembly Overlord | +50% craft amount (stacking) |
| 10 | 300 | Creation Force | +50% craft amount (stacking) |
| 11 | 400 | Transmutation Expert | +50% craft amount (stacking) |
| 12 | 500 | Crafting God | +50% craft amount (stacking) |

**Total bonus at 13/13**: craft amount `×(1 + 13×0.5) = ×7.5`

---

## 18. Skill Milestones — Building

Array: `MS.building` — 13 tiers. Tracked in `S.ms.building`.

| # | Lv Req | Title |
|---|---|---|
| 0 | 5 | Builder Apprentice |
| 1 | 10 | Mason |
| 2 | 25 | Architect |
| 3 | 50 | Engineer |
| 4 | 75 | Master Builder |
| 5 | 100 | Structural Genius |
| 6 | 125 | Tower Designer |
| 7 | 150 | Monument Forger |
| 8 | 200 | City Planner |
| 9 | 250 | Wonder Architect |
| 10 | 300 | Gigalith Crafter |
| 11 | 400 | World Sculptor |
| 12 | 500 | Building God |

**Effect**: Building milestones currently apply to reinforce (if any track ≥4: +0.2, if any ≥8: +0.3).

---

## 19. Skill Milestones — General

Array: `MS.general` — 13 tiers. Tracked in `S.ms.general`.

| # | Lv Req | Title | Effect |
|---|---|---|---|
| 0 | 5 | Learner | — |
| 1 | 10 | Scholar | — |
| 2 | 25 | Savant | ×2 XP multiplier (if ≥2 claimed) |
| 3 | 50 | Genius | — |
| 4 | 75 | Mastermind | — |
| 5 | 100 | Enlightened | — |
| 6 | 125 | Transcendent | — |
| 7 | 150 | Sage of Babel | — |
| 8 | 200 | Demigod | ×4 XP multiplier (if ≥8 claimed) |
| 9 | 250 | Ascended | — |
| 10 | 300 | Cosmic Mind | — |
| 11 | 400 | Universal Force | — |
| 12 | 500 | Omnipotent | — |

---

## 20. Talents — Gathering Branch

Array: `TALENTS` — 4 per branch, 16 total. Max Lv10 each. Cost: `cb × cm^lvl`.

| ID | Name | Icon | Effect per level | Base Cost (cb) | Cost Mult (cm) | Skill Req |
|---|---|---|---|---|---|---|
| t3 | Resource Efficiency | ♻️ | -8% resources per craft (capped 50%) | 80 🪙 | 2.2 | Gathering Lv5 + 3/lv |
| ga2 | Prospector's Eye | 🔍 | +5% chance for bonus resources | 200 🪙 | 2.5 | Gathering Lv10 + 3/lv |
| ga3 | Deep Mining | ⛏️ | +20% more resources per tap | 500 🪙 | 3 | Gathering Lv20 + 5/lv |
| ga4 | Nature's Bounty | 🌿 | +15% auto-gather output | 2,000 🪙 | 4 | Gathering Lv35 + 8/lv |

---

## 21. Talents — Crafting Branch

| ID | Name | Icon | Effect per level | Base Cost | Cost Mult | Skill Req |
|---|---|---|---|---|---|---|
| t4 | Stone Hardening | ⛰️ | -1.2% brick strain (capped 50%) | 150 🪙 | 2.5 | Crafting Lv8 + 3/lv |
| cr2 | Kiln Mastery | 🔥 | +15% craft amount per action | 400 🪙 | 3 | Crafting Lv15 + 4/lv |
| cr3 | Material Fusion | 🔬 | Unlock advanced recipes | 1,500 🪙 | 3.5 | Crafting Lv25 + 5/lv |
| cr4 | Auto-Synthesis | ⚗️ | +15% auto-craft output | 5,000 🪙 | 4.5 | Crafting Lv40 + 10/lv |

---

## 22. Talents — Building Branch

| ID | Name | Icon | Effect per level | Base Cost | Cost Mult | Skill Req |
|---|---|---|---|---|---|---|
| t1 | Scaffolding | 🪜 | +15% build placement speed | 100 🪙 | 2.2 | Building Lv5 + 2/lv |
| t2 | Mortar Mastery | 🧴 | -2% mortar strain (capped 50%) | 200 🪙 | 2.5 | Building Lv10 + 3/lv |
| bl3 | Reinforced Joints | 🔩 | +10% reinforcement bonus | 600 🪙 | 3 | Building Lv20 + 5/lv |
| bl4 | Auto-Architect | 🏗️ | +15% auto-build output | 3,000 🪙 | 4 | Building Lv35 + 8/lv |

---

## 23. Talents — General Branch

| ID | Name | Icon | Effect per level | Base Cost | Cost Mult | Skill Req |
|---|---|---|---|---|---|---|
| t5 | Golden Touch | ✨ | +15% gold from all sources | 300 🪙 | 3 | General Lv10 + 4/lv |
| f1 | Fortress Foundation | 🏛️ | +10% reinforcement mult | 500 🪙 | 3.5 | General Lv15 + 4/lv |
| d1 | Divine Inspiration | 💡 | +15% XP multiplier | 1,000 🪙 | 4 | General Lv25 + 5/lv |
| ge4 | Babel's Blessing | 🔮 | +10% all bonuses multiply | 10,000 🪙 | 5 | General Lv50 + 12/lv |

---

## 24. Prestige Upgrades (P1-P7)

Array: `PR_UPG` — bought with Babel Shards (💎). Cost: `cb × cm^lvl`.

| ID | Name | Icon | Effect per level | Base Cost (💎) | Cost Mult | Max Lv |
|---|---|---|---|---|---|---|
| p1 | Diligent Start | 💰 | +100 starting gold/lv | 1 | 2.2 | 10 |
| p2 | Wider Legacy | 📐 | +1 starting base width/lv | 3 | 3 | 5 |
| p3 | Ancient Foundation | 🏛️ | +3% starting stability/lv | 5 | 3 | 5 |
| p4 | Echoes of Labor | 🔁 | +0.5% extra legacy/lv | 8 | 3.5 | 5 |
| p5 | Eternal Workshop | ⚙️ | +1 auto level all skills/lv | 15 | 4 | 3 |
| p6 | Babel's Memory | 📜 | +5 starting resources/lv | 10 | 3.5 | 5 |
| p7 | Golden Legacy | 👑 | +50% gold all sources/lv | 10 | 3 | 5 |

---

## 25. Prestige Collapse Rewards

Triggered when tower stability ≤ 0% or (stability < 5% and `Math.random() < 0.05 / repairFactor`).

### Legacy
```js
legacy = max(current, floor(tallest_ever × (0.1 + lP('p4') × 0.005)))
```

### Shards
```js
shards = floor(height_at_collapse / 25) + floor(legacy / 10)
```

### Gold bonus
```js
gold = 50 + height_at_collapse × 10 + totalClicks × 0.1
```

---

## 26. Color Constants & Visual Theme

| Constant | Value | Used For |
|---|---|---|
| `GOLD_COL` | `#ffd700` | Gold text, currency displays |
| `RES_COL` | `#c46a3a` | Resource text, gather XP overlay |
| `GXP_COL` | `#e0d0c0` | General XP text |
| `GAT_COL` | `#d06040` | Gathering XP, gather skill |
| `CRA_COL` | `#50b050` | Crafting XP, craft skill |
| `BLD_COL` | `#5090d0` | Building XP, build skill |

### Brick Colors (BC object)

| Brick Type | Base Color (s) | Mid Color (m) | Edge Color (e) |
|---|---|---|---|
| Mud Brick | `#c46a3a` | `#a0522d` | `#8b3a1a` |
| Fired Brick | `#d45030` | `#b83820` | `#8a2010` |
| Stone Block | `#8a8a8a` | `#6a6a6a` | `#4a4a4a` |
| Reinforced Brick | `#6a7a8a` | `#4a5a6a` | `#2a3a4a` |
| Glazed Brick | `#7a8a6a` | `#5a6a4a` | `#3a4a2a` |
| Megalith | `#5a4a3a` | `#3a2a1a` | `#2a1a0a` |
| Mortar | `#b8a890` (m), `#9a8878` (s) | | |

---

## 27. State Object Structure (S)

```javascript
S = {
  res: {},                 // Resources: { mud: number, water: number, ... }
  mat: {},                 // Materials: { mortar: number, mudBrick: number, ... }
  upg: {},                 // All upgrade levels: { g1: number, bp: number, sg1: number, ... }
  tech: {},                // Tower techs owned: { bw1: 6, rf1: 0.2, ... }
  tower: {
    rows: [],              // Array of row objects: [{ bricks: [{st:'e'|'a'|'d'},...], t: timestamp }]
    colCount: 3,           // (legacy) unused
    collapses: 0,          // Total collapses across all runs
    _coll: false,          // Currently collapsed
    tm: 0,                 // Tower milestone bitmask (bit 0 = height 1, bit 1 = height 10, etc.)
    lastRowTime: 0         // Timestamp of last row completion
  },
  burst: {
    power: 20,             // Taps per burst
    speed: 50,             // ms per action during burst
    cost: 20,              // Gold cost per burst activation
    cooldown: 20,          // Seconds per charge recovery
    chrg: 1,               // Current charges available
    lchrg: 1,              // Last known charges (for display)
    last: 0                // Timestamp of last burst
  },
  stat: {
    gold: 0,               // Current gold
    totalClicks: 0,        // Lifetime total taps/clicks
    taps: 0,               // Lifetime build taps
    tallest: 0,            // Tallest tower ever built (rows)
    legacy: 0,             // Cumulative legacy multiplier
    shards: 0              // Current Babel Shards
  },
  sk: {
    gathering: { xp: 0, lv: 1 },
    crafting:  { xp: 0, lv: 1 },
    building:  { xp: 0, lv: 1 },
    general:   { xp: 0, lv: 1 }
  },
  ms: {
    gathering: 0,          // Number of gathering milestones claimed (0-13)
    crafting: 0,           // Number of crafting milestones claimed
    building: 0,           // Number of building milestones claimed
    general: 0             // Number of general milestones claimed
  },
  tal: {},                 // Talent levels: { t3: number, ga2: number, ... }
  tick: 0,                 // Global tick counter (increments every 100ms)
  _selCraft: null,         // Currently selected craft recipe ID
  auto: {
    gather: 0,             // Auto-gather level
    craft: 0,              // Auto-craft level
    build: 0               // Auto-build level
  },
  autoCraftTick: 0,        // Tick counter for auto-craft scheduling
  pr: {},                  // Prestige levels: { p1: number, p2: number, ... }
  lastSave: 0              // Timestamp of last save
}
```

---

## 28. Tracked Statistics

| Stat | Variable | Type | Persists After Collapse? |
|---|---|---|---|
| Gold | `S.stat.gold` | number | Yes |
| Total Clicks | `S.stat.totalClicks` | number | Yes |
| Build Taps | `S.stat.taps` | number | Yes |
| Tallest Tower | `S.stat.tallest` | number (rows) | Yes |
| Legacy | `S.stat.legacy` | number | Yes |
| Babel Shards | `S.stat.shards` | number | Yes |
| Collapses | `S.tower.collapses` | number | Yes |
| Tower Height | `S.tower.rows.length` | number (rows) | No (reset on collapse) |
| Tower Milestones | `S.tower.tm` | bitmask | Yes |
| Burst Charges | `S.burst.chrg` | number | Yes |
| Skill Levels | `S.sk[id].lv` | number | Yes |
| Skill XP | `S.sk[id].xp` | number | Yes |

---

## 29. Helper Functions

| Function | Purpose | Formula |
|---|---|---|
| `uL(id)` | Upgrade level | `S.upg[id] \|\| 0` |
| `tL(id)` | Talent level | `S.tal[id] \|\| 0` |
| `msG(id)` | Milestones claimed | `S.ms[id] \|\| 0` |
| `skLv(id)` | Skill level | `S.sk[id]?.lv \|\| 1` |
| `aL(id)` | Auto upgrade level | `S.auto[id] \|\| 0` |
| `lP(id)` | Prestige level | `S.pr?.[id] \|\| 0` |
| `xpN(lv)` | XP to next level | `floor(50 × lv × (1 + 0.12 × lv))` |
| `fmt(n)` | Number formatting | 1.1K → 1.1M → 1.1B |
| `rC(id)` | Recalculate skill level from XP | Descending XP check |
| `towerMsClaimed(type)` | Tower milestone count | Bitmask check on `S.tower.tm` |
| `checkTowerMs()` | Auto-claim tower milestones | Check height against TOWER_MS |
| `burstLv(id)` | Burst upgrade level (capped) | `min(S.upg[id], maxLv)` |
| `getBurstPower()` | Current burst power | `20 + burstLv('bp') × 20` |
| `getBurstSpeed()` | Current burst speed | `max(10, 50 - burstLv('bs') × 5)` |
| `getBurstCost()` | Current burst gold cost | `max(0, 20 - burstLv('bc') × 2)` |
| `getBurstCooldown()` | Current burst cooldown | `max(2, 20 - burstLv('bcd') × 2)` |
| `getBurstCharges()` | Max burst charges | `1 + burstLv('bch')` |
| `rechargeBurst()` | Passive charge recovery | Called every 100ms tick |

---

## 30. Tower Stability Formula

### Base Width
```js
baseWidth = S.tech.bwN || (20 + lP('p2'))
// Tower milestone bonus: if towerMsClaimed('width') > 0, multiply by 1.1
```

### Reinforce Score
```js
reinforce = 0
  + lP('p3') × 0.03               // Prestige foundation
  + Σ(rf_tech_values)             // rf1=0.2 through rf5=1.0
  × (1 + tL('f1') × 0.1)          // Fortress Foundation talent
  × (1 + tL('bl3') × 0.1)         // Reinforced Joints talent
  + (any milestone ≥4 ? 0.2 : 0)
  + (any milestone ≥8 ? 0.3 : 0)
```

### Foundation Multiplier
```js
foundationMult = 1
  + Σ(fd_tech_values)             // fd1=0.5, fd2=1.0, fd3=2.0
// Tower milestone: ×2 per towerMsClaimed('foundation')
```

### Material Strength
```js
materialStr = MAT_ALL[currentMat].str  // 1.0 (mud) → 0.2 (megalith)
adjustedStr = materialStr 
  × max(0.5, 1 - (tL('t2')×0.02 + tL('t4')×0.012))  // mortar+brick talents
```

### Max Safe Height
```js
maxSafe = baseWidth × 5 + 25 + reinforce × 30 + foundationMult × 10
```

### Stability Percentage
```js
stability = phaseShift => max(0, min(100, 100 - (height / maxSafe) × 100))
// Tower milestone: +5 per towerMsClaimed('stability')
```

### Collapse Trigger
```js
if (stability ≤ 0 || (stability < 5 && Math.random() < 0.05 / repairFactor)) {
  // COLLAPSE: award shards + legacy + gold, reset tower
}
// repairFactor = towerMsClaimed('repair') > 0 ? 3 : 1
```

---

## 31. XP & Leveling Formulas

### XP Required for Level
```js
xpN(lv) = floor(50 × lv × (1 + 0.12 × lv))
```

### XP TNL Table (selected)

| Level | XP Required | Cumulative from Lv1 |
|---|---|---|
| 1 | 56 | 56 |
| 5 | 400 | 1,200 |
| 10 | 1,100 | 5,775 |
| 25 | 5,000 | 68,750 |
| 50 | 17,500 | 388,750 |
| 75 | 37,500 | 1,228,750 |
| 100 | 65,000 | 2,868,750 |
| 150 | 142,500 | 9,758,750 |
| 200 | 250,000 | 22,733,750 |
| 300 | 555,000 | 70,283,750 |
| 500 | 1,525,000 | 270,433,750 |

### XP Earned Per Action

| Action | Skill XP | General XP |
|---|---|---|
| Gather tap | 1 × DB | 0.5 × DB |
| Craft tap | 2 × DB | 1 × DB |
| Build tap (position) | 1 × DB | — |
| Build tap (place) | 2 × DB | 1 × DB |
| Skills tab tap | — | 1 × DB |

### XP Multiplier Stack
```js
earnX(skill, base) {
  m = 1
  if (msG('general') ≥ 2) m ×= 2
  if (msG('general') ≥ 8) m ×= 4
  if (skill === 'gathering' && sgLv > 0) m ×= (1 + sgLv)
  if (skill === 'crafting'  && scLv > 0) m ×= (1 + scLv)
  if (skill === 'building'  && sbLv > 0) m ×= (1 + sbLv)
  if (tL('d1') > 0)  m ×= (1 + tL('d1') × 0.15)
  if (tL('ge4') > 0) m ×= (1 + tL('ge4') × 0.1)
  if (legacy > 0)    m ×= (1 + legacy × 0.01)
  return floor(base × m)
}
```

---

## 32. Gold Generation Formulas

### Gather Gold
```js
baseGatherGold = 1
milestoneMult = max(1, 1 + msG('gathering') × 0.5)
tapUpgradeMult = 1 + 0.5×gLv(g1) + 1.0×gLv(g2) + 2.0×gLv(g3) + 4.0×gLv(g4)
prestigeMult = 1 + lP('p7') × 0.5
allMult = tL('ge4') > 0 ? 1 + tL('ge4') × 0.1 : 1
goldMult = tL('t5') > 0 ? 1 + tL('t5') × 0.15 : 1

gatherGold = floor(1 × milestoneMult × tapUpgradeMult × prestigeMult × allMult × goldMult)
```

### Craft Gold
```js
craftGold = floor(
  materialTier × (1 + 0.5×cLv(c1) + 1.0×cLv(c2) + 2.0×cLv(c3) + 4.0×cLv(c4))
  × prestigeMult × allMult × goldMult
)
```

### Building Gold (brick placement)
```js
buildGold = floor((Math.random()×3 + 1) × DB
  × (towerMsClaimed('gold') > 0 ? 2 : 1)
  × allMult × goldMult)
```

---

## 33. Automation Interval Formulas

### Base Interval
```js
getAutoInterval(skillLevel) {
  lv = min(aL(skill), 15)
  return max(100, 3000 / (1 + 0.5 × lv))  // in milliseconds
}
```

### Auto Interval Table

| Effective Level | Interval (ms) | Actions/min |
|---|---|---|
| 1 | 2,000 | 30 |
| 2 | 1,500 | 40 |
| 3 | 1,200 | 50 |
| 4 | 1,000 | 60 |
| 5 | 857 | 70 |
| 6 | 750 | 80 |
| 7 | 667 | 90 |
| 8 | 600 | 100 |
| 9 | 545 | 110 |
| 10 | 500 | 120 |
| 11 | 462 | 130 |
| 12 | 429 | 140 |
| 13 | 400 | 150 |
| 14 | 375 | 160 |
| 15 | 353 | 170 |

p5 (Eternal Workshop) adds effective levels: p5 Lv1→+1, Lv2→+2, Lv3→+3

---

## 34. Cost Scaling Formulas

### Standard Upgrades (geometric)
```js
cost(level) = floor(baseCost × multiplier^level)
```
Used by: G1-G4, C1-C4, R1-R6, AG1-AB3, SG1-SB3, all talents, all prestige

### Flat Cost Tech
```js
cost = flat_price  // one-time purchase
```
Used by: BW1-BW6, RF1-RF5, FD1-FD3

### Burst Upgrades (geometric)
```js
cost(level) = floor(cb × cm^level)
```
Used by: BP, BS, BC, BCD, BCH

---

## 35. Burst Engine Formulas

### Charge Recovery
```js
// Called every 100ms game tick
rechargeBurst():
  maxCh = getBurstCharges()
  if (lchrg ≥ maxCh) return
  cooldownMS = getBurstCooldown() × 1000
  timeSinceLast = Date.now() - lastBurstTime
  if (timeSinceLast ≥ cooldownMS):
    gained = floor(timeSinceLast / cooldownMS)
    lchrg = min(maxCh, lchrg + gained)
    lastBurstTime = Date.now()
    if (chrg < lchrg) chrg = lchrg
```

### Burst Activation
```js
buildBurst():
  if (lchrg < 1) → "No charges"
  if (gold < cost) → "Need gold"
  if (stability < 15%) → "Too unstable"
  deduct charge + cost
  fire `power` taps at `speed` ms intervals
```

### Burst Throughput Table

| Upgrades | Power | Speed | Duration | Cooldown | Charges | Sustained taps/s |
|---|---|---|---|---|---|---|
| Base | 20 | 50ms | 1.0s | 20s | 1 | 0.95 |
| Lv3 each | 80 | 35ms | 2.8s | 14s | 1 | 5.7 |
| Lv5 each | 120 | 25ms | 3.0s | 10s | 2 | 24.0 |
| Lv8 each | 180 | 10ms | 1.8s | 4s | 4 | 90.0 |
| Maxed | 220 | 10ms | 2.2s | 2s | 6 | 110.0 |

---

## 36. Input Methods & UI Bindings

| UI Element | Tap Action | Hold Action | Keybind |
|---|---|---|---|
| Gather zone | `gather(gF().id)` | Hold-to-repeat (120ms) | — |
| Craft zone | `craft(autoCraft())` | Hold-to-repeat (120ms) | — |
| Build overlay | `tapBuild()` | Hold-to-repeat (120ms) | — |
| Canvas (tower) | `tapBuild()` | — | Space, Enter |
| Burst button | `buildBurst()` | — | — |
| Skills tab | `tapSkills()` | Hold-to-repeat (120ms) | 4 |
| Talents tab | `tapTalents()` | Hold-to-repeat (120ms) | 5 |
| Ascend tab | `tapAscend()` | — | 6 |
| Tab switch | — | — | 1-6 |

---

## 37. Debug Mode Controls

Available from the ⚙️ Options panel (gear icon in top bar):

| Control | Effect |
|---|---|
| **DB ON/OFF** | Toggle 10× multiplier on all gains (DB=10 vs DB=1) |
| **Unlimited Resources ON/OFF** | Toggle free crafting (resources not consumed) |

Both can be toggled independently during gameplay.

---

## 38. Save System

| Aspect | Detail |
|---|---|
| Storage | `localStorage` key `'babel_save'` |
| Serialization | `JSON.stringify(S)` full state |
| Save interval | Every 5 seconds (`setInterval(save, 5000)`) |
| Load timing | On page load, in `init()` → `load()` |
| Offline progress | Up to 24h calculated on load |
| Export | Copy save to clipboard via Options |
| Reset | Confirm dialog → `localStorage.removeItem` → reload |

### Offline Progress Calculation
```js
ticks = min(elapsed_ms, 86400000) / 100
autoGathers = floor(ticks / (gatherInterval / 100))
autoCrafts  = floor(ticks / (craftInterval / 100))
autoBuilds  = min(floor(ticks / (buildInterval / 100)), 500)
```

---

## 39. Tab Structure

6 tabs, navigable via bottom bar or keyboard (1-6):

| # | ID | Content |
|---|---|---|
| 1 | `gather` | Resource grid (4 cols), tap zone, auto status |
| 2 | `craft` | Auto-selected recipe, resource costs, tap zone |
| 3 | `build` | Canvas (tower visualization), HUD (height/width/stability), burst panel, tech panel, tap overlay |
| 4 | `skills` | Skill XP bars, milestones (next 2 visible), skill upgrades (4 sets), talent grid |
| 5 | `talents` | 16 talents in 4 branches, tap zone |
| 6 | `ascend` | Collapse stats, prestige upgrades (7), tap zone |

Each pane uses `.pane.on` / `.pane` CSS classes for visibility.

---

## 40. Animation & Visual Systems

### Canvas Rendering (requestAnimationFrame loop)

| Visual Element | Description |
|---|---|
| Sky gradient | Height-dependent gradient shift (0.3 → 0.6 sky fraction) |
| Stars | Random dots, more at greater heights |
| Ground | Dark platform with subtle edge line |
| Tower rows | Animated entry (0.3→1.0 scale over 400ms) |
| Brick states | Empty (`e`), hovering (`a` with bob), placed (`d`) |
| Pillars | Side pillars rendered per row |
| Mortar lines | Between-row mortar rendering |
| Cracks | Visible at stability < 25%, intensity scales |
| Tower sway | Lateral sway at stability < 30% |
| Collapse particles | Orange/red particle burst on collapse |
| Holding ghost | Semi-transparent brick at mouse position |

### CSS Animations

| Animation | Timing | Purpose |
|---|---|---|
| `feedUp` | 800ms | Floating tap feedback (+res, +gold, +XP) |
| `celebPulse` | 600ms | Level-up celebration |
| `glowPulse` | 2s | Resource highlight pulse |
| `shake` | 500ms | Tower collapse screen shake |
| XP overlay | 1200ms | Skill bar expansion on XP gain |
| Particle burst | 600ms | Level-up sparkle stars |

### Feedback Systems

| System | Trigger | Display |
|---|---|---|
| Feed popup | Every tap (`showFeed`) | Colored floating text near tap position (100px range) |
| Notification | Significant events (`notif`) | Top-center bar, 1.5s auto-dismiss |
| Level-up | Skill level change (`showCeleb`) | Color-coded text + 8 particle stars |
| Stability bar | Build tab HUD | Color-coded bar (green→yellow→red) |
| Brick dots | Build tab row display | Green dot = placed, empty = unplaced, red crack = damaged |

---

*End of Complete Game Systems Catalog. 1,106 lines.*

---

## 41. Full Upgrade Cost Tables — Every Level

### 41.1 Gather Gold Upgrades (G1-G4)

#### G1 — Clay Fingers
| Level | Cost 🪙 | Cumulative | Gold per Gather |
|---|---|---|---|
| 1 | 20 | 20 | ×1.5 |
| 2 | 50 | 70 | ×2.0 |
| 3 | 125 | 195 | ×2.5 |
| 4 | 312 | 507 | ×3.0 |
| 5 | 781 | 1,288 | ×3.5 |
| 6 | 1,953 | 3,241 | ×4.0 |
| 7 | 4,882 | 8,123 | ×4.5 |
| 8 | 12,207 | 20,330 | ×5.0 |
| 9 | 30,517 | 50,847 | ×5.5 |
| 10 | 76,293 | 127,140 | ×6.0 |

#### G2 — Sharp Eye
| Level | Cost 🪙 | Cumulative | Gold per Gather |
|---|---|---|---|
| 1 | 80 | 80 | +1 |
| 2 | 240 | 320 | +2 |
| 3 | 720 | 1,040 | +3 |
| 4 | 2,160 | 3,200 | +4 |
| 5 | 6,480 | 9,680 | +5 |
| 6 | 19,440 | 29,120 | +6 |
| 7 | 58,320 | 87,440 | +7 |
| 8 | 174,960 | 262,400 | +8 |
| 9 | 524,880 | 787,280 | +9 |
| 10 | 1,574,640 | 2,361,920 | +10 |

#### G3 — Iron Will
| Level | Cost 🪙 | Cumulative | Gold per Gather |
|---|---|---|---|
| 1 | 300 | 300 | +2 |
| 2 | 960 | 1,260 | +4 |
| 3 | 3,072 | 4,332 | +6 |
| 4 | 9,830 | 14,162 | +8 |
| 5 | 31,457 | 45,619 | +10 |
| 6 | 100,663 | 146,282 | +12 |
| 7 | 322,122 | 468,404 | +14 |
| 8 | 1,030,792 | 1,499,196 | +16 |
| 9 | 3,298,534 | 4,797,730 | +18 |
| 10 | 10,555,311 | 15,353,041 | +20 |

#### G4 — Stone Hands
| Level | Cost 🪙 | Cumulative | Gold per Gather |
|---|---|---|---|
| 1 | 1,000 | 1,000 | +4 |
| 2 | 3,500 | 4,500 | +8 |
| 3 | 12,250 | 16,750 | +12 |
| 4 | 42,875 | 59,625 | +16 |
| 5 | 150,062 | 209,687 | +20 |
| 6 | 525,218 | 734,905 | +24 |
| 7 | 1,838,265 | 2,573,170 | +28 |
| 8 | 6,433,929 | 9,007,099 | +32 |
| 9 | 22,518,753 | 31,525,852 | +36 |
| 10 | 78,815,638 | 110,341,490 | +40 |

### 41.2 Craft Gold Upgrades (C1-C4)

#### C1 — Quick Mix
| Level | Cost 🪙 | Cumulative | Gold Mult (tier×) |
|---|---|---|---|
| 1 | 25 | 25 | ×1.5 |
| 2 | 62 | 87 | ×2.0 |
| 3 | 156 | 243 | ×2.5 |
| 4 | 390 | 633 | ×3.0 |
| 5 | 976 | 1,609 | ×3.5 |
| 6 | 2,441 | 4,050 | ×4.0 |
| 7 | 6,103 | 10,153 | ×4.5 |
| 8 | 15,258 | 25,411 | ×5.0 |
| 9 | 38,146 | 63,557 | ×5.5 |
| 10 | 95,367 | 158,924 | ×6.0 |

#### C2 — Efficient Kiln
| Level | Cost 🪙 | Cumulative |
|---|---|---|
| 1 | 100 | 100 |
| 2 | 300 | 400 |
| 3 | 900 | 1,300 |
| 4 | 2,700 | 4,000 |
| 5 | 8,100 | 12,100 |
| 6 | 24,300 | 36,400 |
| 7 | 72,900 | 109,300 |
| 8 | 218,700 | 328,000 |
| 9 | 656,100 | 984,100 |
| 10 | 1,968,300 | 2,952,400 |

#### C3 — Assembly Line
| Level | Cost 🪙 | Cumulative |
|---|---|---|
| 1 | 400 | 400 |
| 2 | 1,280 | 1,680 |
| 3 | 4,096 | 5,776 |
| 4 | 13,107 | 18,883 |
| 5 | 41,943 | 60,826 |
| 6 | 134,217 | 195,043 |
| 7 | 429,496 | 624,539 |
| 8 | 1,374,389 | 1,998,928 |
| 9 | 4,398,046 | 6,396,974 |
| 10 | 14,073,748 | 20,470,722 |

#### C4 — Auto-Forge
| Level | Cost 🪙 | Cumulative |
|---|---|---|
| 1 | 1,500 | 1,500 |
| 2 | 5,250 | 6,750 |
| 3 | 18,375 | 25,125 |
| 4 | 64,312 | 89,437 |
| 5 | 225,093 | 314,530 |
| 6 | 787,825 | 1,102,355 |
| 7 | 2,757,396 | 3,859,751 |
| 8 | 9,650,886 | 13,510,637 |
| 9 | 33,778,130 | 47,288,767 |
| 10 | 118,223,458 | 165,512,225 |

### 41.3 Resource % Upgrades (R1-R6)

#### R1 — Rustic Tools
| Level | Cost 🪙 | Cumulative | Resource Mult |
|---|---|---|---|
| 1 | 50 | 50 | +10% |
| 2 | 140 | 190 | +20% |
| 3 | 391 | 581 | +30% |
| 4 | 1,097 | 1,678 | +40% |
| 5 | 3,073 | 4,751 | +50% |
| 6 | 8,605 | 13,356 | +60% |
| 7 | 24,095 | 37,451 | +70% |
| 8 | 67,468 | 104,919 | +80% |
| 9 | 188,912 | 293,831 | +90% |
| 10 | 528,955 | 822,786 | +100% |
| 11 | 1,481,076 | 2,303,862 | +110% |
| 12 | 4,147,014 | 6,450,876 | +120% |
| 13 | 11,611,639 | 18,062,515 | +130% |
| 14 | 32,512,590 | 50,575,105 | +140% |
| 15 | 91,026,255 | 141,601,360 | +150% |

#### R2 — Ox Cart
| Level | Cost 🪙 | Cumulative | Resource Mult |
|---|---|---|---|
| 1 | 200 | 200 | +15% |
| 5 | 20,971 | 31,124 | +75% |
| 10 | 21,990,232 | 31,315,681 | +150% |
| 15 | 2,361,183,241 | 3,434,448,254 | +225% |

#### R3 — Water Wheel
| Level | Cost 🪙 | Cumulative | Resource Mult |
|---|---|---|---|
| 1 | 800 | 800 | +20% |
| 5 | 120,050 | 175,693 | +100% |
| 10 | 282,475,249 | 399,623,013 | +200% |
| 15 | 33,116,360,978 | 46,362,905,045 | +300% |

#### R4 — Crane
| Level | Cost 🪙 | Cumulative | Resource Mult |
|---|---|---|---|
| 1 | 3,000 | 3,000 | +30% |
| 5 | 768,000 | 1,023,000 | +150% |
| 10 | 805,306,368,000 | 1,073,741,823,000 | +300% |

#### R5 — Steam Engine
| Level | Cost 🪙 | Resource Mult |
|---|---|---|
| 1 | 12,000 | +50% |
| 5 | 4,920,750 | +250% |
| 10 | — | +500% |

#### R6 — Magic Loom
| Level | Cost 🪙 | Resource Mult |
|---|---|---|
| 1 | 5,000 | +100% |
| 5 | 750,312 | +500% |
| 10 | 59,136,358,890 | +1,000% |
| 15 | 206,977,256,118 | +1,500% |

### 41.4 Auto Upgrade Costs

#### AG1 — Auto-Scoop (Gather)
| Level | Cost 🪙 | Cumulative | Auto Interval |
|---|---|---|---|
| 1 | 80 | 80 | 2,000ms |
| 2 | 224 | 304 | 1,500ms |
| 3 | 627 | 931 | 1,200ms |
| 4 | 1,756 | 2,687 | 1,000ms |
| 5 | 4,917 | 7,604 | 857ms |
| 6 | 13,768 | 21,372 | 750ms |
| 7 | 38,552 | 59,924 | 667ms |
| 8 | 107,946 | 167,870 | 600ms |
| 9 | 302,247 | 470,117 | 545ms |
| 10 | 846,276 | 1,316,393 | 500ms |

#### AC1 — Auto-Stir (Craft)
| Level | Cost 🪙 | Cumulative | Interval |
|---|---|---|---|
| 1 | 120 | 120 | 2,000ms |
| 2 | 336 | 456 | 1,500ms |
| 3 | 940 | 1,396 | 1,200ms |
| 4 | 2,634 | 4,030 | 1,000ms |
| 5 | 7,375 | 11,405 | 857ms |
| 6 | 20,651 | 32,056 | 750ms |
| 7 | 57,823 | 89,879 | 667ms |
| 8 | 161,903 | 251,782 | 600ms |
| 9 | 453,362 | 705,144 | 545ms |
| 10 | 1,269,414 | 1,974,558 | 500ms |

#### AB1 — Auto-Trowel (Build)
| Level | Cost 🪙 | Cumulative | Interval |
|---|---|---|---|
| 1 | 200 | 200 | 2,000ms |
| 2 | 560 | 760 | 1,500ms |
| 3 | 1,567 | 2,327 | 1,200ms |
| 4 | 4,390 | 6,717 | 1,000ms |
| 5 | 12,293 | 19,010 | 857ms |
| 6 | 34,421 | 53,431 | 750ms |
| 7 | 96,380 | 149,811 | 667ms |
| 8 | 269,869 | 419,680 | 600ms |
| 9 | 755,603 | 1,175,283 | 545ms |
| 10 | 2,115,691 | 3,290,974 | 500ms |

#### AG2 — Auto-Windmill
| 1 | 500 | 500 | Faster interval |
| 5 | 52,428 | 83,886 | — |
| 10 | 17,592,186 | 25,588,402 | — |

#### AG3 — Auto-Earth Mover
| 1 | 3,000 | 3,000 | Fastest interval |
| 5 | 625,540 | 936,103 | — |
| 10 | 495,648,303 | 672,664,480 | — |

### 41.5 Skill XP Upgrade Costs

#### SG1/SC1/SB1 — Focus (×2 rate)
| Level | Cost 🪙 | Cumulative | XP Mult |
|---|---|---|---|
| 1 | 100 | 100 | ×2 |
| 2 | 250 | 350 | ×3 |
| 3 | 625 | 975 | ×4 |
| 4 | 1,562 | 2,537 | ×5 |
| 5 | 3,906 | 6,443 | ×6 |
| 6 | 9,765 | 16,208 | ×7 |
| 7 | 24,414 | 40,622 | ×8 |
| 8 | 61,035 | 101,657 | ×9 |
| 9 | 152,587 | 254,244 | ×10 |
| 10 | 381,469 | 635,713 | ×11 |

#### SG2/SC2/SB2 — Mastery (×3 rate)
| 1 | 2,000 | 2,000 | ×3 |
| 5 | 512,000 | 682,000 | ×15 |
| 10 | 524,288,000 | 699,050,000 | ×31 |

#### SG3/SC3/SB3 — Supremacy (×5 rate)
| 1 | 20,000 | 20,000 | ×5 |
| 5 | 12,500,000 | 15,621,000 | ×25 |
| 10 | 39,062,500,000 | 48,828,120,000 | ×51 |

### 41.6 Burst Engine Upgrade Costs

#### BP — Crane Power
| Level | Cost 🪙 | Cumulative | Power |
|---|---|---|---|
| 1 | 200 | 200 | 40 taps |
| 2 | 500 | 700 | 60 taps |
| 3 | 1,250 | 1,950 | 80 taps |
| 4 | 3,125 | 5,075 | 100 taps |
| 5 | 7,812 | 12,887 | 120 taps |
| 6 | 19,531 | 32,418 | 140 taps |
| 7 | 48,828 | 81,246 | 160 taps |
| 8 | 122,070 | 203,316 | 180 taps |
| 9 | 305,175 | 508,491 | 200 taps |
| 10 | 762,939 | 1,271,430 | 220 taps |

#### BS — Pulley Speed
| Level | Cost 🪙 | Cumulative | Speed |
|---|---|---|---|
| 1 | 400 | 400 | 45ms |
| 2 | 1,120 | 1,520 | 40ms |
| 3 | 3,135 | 4,655 | 35ms |
| 4 | 8,780 | 13,435 | 30ms |
| 5 | 24,586 | 38,021 | 25ms |
| 6 | 68,841 | 106,862 | 20ms |
| 7 | 192,756 | 299,618 | 15ms |
| 8 | 539,717 | 839,335 | 10ms |

#### BC — Bulk Order
| Level | Cost 🪙 | Cumulative | Cost per Burst |
|---|---|---|---|
| 1 | 300 | 300 | 18🪙 |
| 2 | 750 | 1,050 | 16🪙 |
| 3 | 1,875 | 2,925 | 14🪙 |
| 4 | 4,687 | 7,612 | 12🪙 |
| 5 | 11,718 | 19,330 | 10🪙 |
| 6 | 29,296 | 48,626 | 8🪙 |
| 7 | 73,242 | 121,868 | 6🪙 |
| 8 | 183,105 | 304,973 | 4🪙 |
| 9 | 457,763 | 762,736 | 2🪙 |
| 10 | 1,144,409 | 1,907,145 | 0🪙 |

#### BCD — Crew Cooldown
| Level | Cost 🪙 | Cumulative | Cooldown |
|---|---|---|---|
| 1 | 500 | 500 | 18s |
| 2 | 1,500 | 2,000 | 16s |
| 3 | 4,500 | 6,500 | 14s |
| 4 | 13,500 | 20,000 | 12s |
| 5 | 40,500 | 60,500 | 10s |
| 6 | 121,500 | 182,000 | 8s |
| 7 | 364,500 | 546,500 | 6s |
| 8 | 1,093,500 | 1,640,000 | 4s |
| 9 | 3,280,500 | 4,920,500 | 2s |

#### BCH — Reserve Crew
| Level | Cost 🪙 | Cumulative | Max Charges |
|---|---|---|---|
| 1 | 1,000 | 1,000 | 2 |
| 2 | 3,500 | 4,500 | 3 |
| 3 | 12,250 | 16,750 | 4 |
| 4 | 42,875 | 59,625 | 5 |
| 5 | 150,062 | 209,687 | 6 |

### 41.7 Tech Costs (One-Time)

| Tech | Cost 🪙 | Effect |
|---|---|---|
| bw1 | 100 | Width → 6 |
| bw2 | 500 | Width → 10 |
| bw3 | 2,500 | Width → 15 |
| bw4 | 15,000 | Width → 20 |
| bw5 | 100,000 | Width → 30 |
| bw6 | 500,000 | Width → 50 (risky) |
| rf1 | 200 | +0.20 stability |
| rf2 | 1,000 | +0.40 stability |
| rf3 | 5,000 | +0.60 stability |
| rf4 | 30,000 | +0.80 stability |
| rf5 | 200,000 | +1.00 stability |
| fd1 | 1,000 | ×1.5 strength |
| fd2 | 8,000 | ×2.0 strength |
| fd3 | 60,000 | ×3.0 strength |

### 41.8 Prestige Shard Costs (Every Level)

#### P1 — Diligent Start
| Level | Cost 💎 | Cumulative | Effect |
|---|---|---|---|
| 1 | 1 | 1 | +100 starting gold |
| 2 | 2 | 3 | +200 |
| 3 | 4 | 7 | +300 |
| 4 | 10 | 17 | +400 |
| 5 | 23 | 40 | +500 |
| 6 | 51 | 91 | +600 |
| 7 | 113 | 204 | +700 |
| 8 | 249 | 453 | +800 |
| 9 | 548 | 1,001 | +900 |
| 10 | 1,207 | 2,208 | +1,000 |

#### P2 — Wider Legacy
| Level | Cost 💎 | Cumulative | Effect |
|---|---|---|---|
| 1 | 3 | 3 | +1 width |
| 2 | 9 | 12 | +2 width |
| 3 | 27 | 39 | +3 width |
| 4 | 81 | 120 | +4 width |
| 5 | 243 | 363 | +5 width |

#### P3 — Ancient Foundation
| Level | Cost 💎 | Cumulative | Effect |
|---|---|---|---|
| 1 | 5 | 5 | +3% stability |
| 2 | 15 | 20 | +6% |
| 3 | 45 | 65 | +9% |
| 4 | 135 | 200 | +12% |
| 5 | 405 | 605 | +15% |

#### P4 — Echoes of Labor
| Level | Cost 💎 | Cumulative | Effect |
|---|---|---|---|
| 1 | 8 | 8 | +0.5% legacy/lv |
| 2 | 28 | 36 | +1.0% |
| 3 | 98 | 134 | +1.5% |
| 4 | 343 | 477 | +2.0% |
| 5 | 1,200 | 1,677 | +2.5% |

#### P5 — Eternal Workshop
| Level | Cost 💎 | Cumulative | Effect |
|---|---|---|---|
| 1 | 15 | 15 | +1 auto level |
| 2 | 60 | 75 | +2 auto levels |
| 3 | 240 | 315 | +3 auto levels |

#### P6 — Babel's Memory
| Level | Cost 💎 | Cumulative | Effect |
|---|---|---|---|
| 1 | 10 | 10 | +5 each resource |
| 2 | 35 | 45 | +10 |
| 3 | 122 | 167 | +15 |
| 4 | 428 | 595 | +20 |
| 5 | 1,500 | 2,095 | +25 |

#### P7 — Golden Legacy
| Level | Cost 💎 | Cumulative | Effect |
|---|---|---|---|
| 1 | 10 | 10 | +50% gold |
| 2 | 30 | 40 | +100% |
| 3 | 90 | 130 | +150% |
| 4 | 270 | 400 | +200% |
| 5 | 810 | 1,210 | +250% |

---

## 42. Full Talent Cost Tables (Every Level)

### 42.1 Gathering Branch

#### T3 — Resource Efficiency
| Level | Cost 🪙 | Cumulative | Resource Save | Skill Req |
|---|---|---|---|---|
| 1 | 80 | 80 | 8% | Gather Lv8 |
| 2 | 176 | 256 | 16% | Gather Lv11 |
| 3 | 387 | 643 | 24% | Gather Lv14 |
| 4 | 851 | 1,494 | 32% | Gather Lv17 |
| 5 | 1,874 | 3,368 | 40% | Gather Lv20 |
| 6 | 4,123 | 7,491 | 48% | Gather Lv23 |
| 7 | 9,071 | 16,562 | 50% (capped) | Gather Lv26 |
| 8 | 19,958 | 36,520 | 50% | Gather Lv29 |
| 9 | 43,900 | 80,420 | 50% | Gather Lv32 |
| 10 | 96,581 | 177,001 | 50% | Gather Lv35 |

#### GA2 — Prospector's Eye
| Level | Cost 🪙 | Cumulative | Rare Chance | Skill Req |
|---|---|---|---|---|
| 1 | 200 | 200 | 5% | Gather Lv13 |
| 2 | 500 | 700 | 10% | Gather Lv16 |
| 3 | 1,250 | 1,950 | 15% | Gather Lv19 |
| 4 | 3,125 | 5,075 | 20% | Gather Lv22 |
| 5 | 7,812 | 12,887 | 25% | Gather Lv25 |
| 6 | 19,531 | 32,418 | 30% | Gather Lv28 |
| 7 | 48,828 | 81,246 | 35% | Gather Lv31 |
| 8 | 122,070 | 203,316 | 40% | Gather Lv34 |
| 9 | 305,175 | 508,491 | 45% | Gather Lv37 |
| 10 | 762,939 | 1,271,430 | 50% | Gather Lv40 |

#### GA3 — Deep Mining
| Level | Cost 🪙 | Cumulative | Gather Mult | Skill Req |
|---|---|---|---|---|
| 1 | 500 | 500 | +20% | Gather Lv25 |
| 2 | 1,500 | 2,000 | +40% | Gather Lv30 |
| 3 | 4,500 | 6,500 | +60% | Gather Lv35 |
| 4 | 13,500 | 20,000 | +80% | Gather Lv40 |
| 5 | 40,500 | 60,500 | +100% | Gather Lv45 |
| 6 | 121,500 | 182,000 | +120% | Gather Lv50 |
| 7 | 364,500 | 546,500 | +140% | Gather Lv55 |
| 8 | 1,093,500 | 1,640,000 | +160% | Gather Lv60 |
| 9 | 3,280,500 | 4,920,500 | +180% | Gather Lv65 |
| 10 | 9,841,500 | 14,762,000 | +200% | Gather Lv70 |

#### GA4 — Nature's Bounty
| Level | Cost 🪙 | Auto-Gather Mult | Skill Req |
|---|---|---|---|
| 1 | 2,000 | +15% | Gather Lv43 |
| 2 | 8,000 | +30% | Gather Lv51 |
| 3 | 32,000 | +45% | Gather Lv59 |
| 4 | 128,000 | +60% | Gather Lv67 |
| 5 | 512,000 | +75% | Gather Lv75 |
| 10 | 524,288,000 | +150% | Gather Lv115 |

### 42.2 Crafting Branch

#### T4 — Stone Hardening
| Level | Cost 🪙 | Brick Str Reduction | Craft Req |
|---|---|---|---|
| 1 | 150 | -1.2% | Craft Lv11 |
| 2 | 375 | -2.4% | Craft Lv14 |
| 3 | 937 | -3.6% | Craft Lv17 |
| 4 | 2,343 | -4.8% | Craft Lv20 |
| 5 | 5,859 | -6.0% | Craft Lv23 |
| 10 | 572,204 | -12% (capped) | Craft Lv38 |

#### CR2 — Kiln Mastery
| Level | Cost 🪙 | Craft Speed | Craft Req |
|---|---|---|---|
| 1 | 400 | +15% | Craft Lv19 |
| 5 | 32,400 | +75% | Craft Lv35 |
| 10 | 7,873,200 | +150% | Craft Lv55 |

#### CR3 — Material Fusion
| Level | Cost 🪙 | Recipe Tier | Craft Req |
|---|---|---|---|
| 1 | 1,500 | +0.1 | Craft Lv28 |
| 5 | 225,093 | +0.5 | Craft Lv45 |
| 10 | 118,223,458 | +1.0 | Craft Lv65 |

#### CR4 — Auto-Synthesis
| Level | Cost 🪙 | Auto-Craft Mult | Craft Req |
|---|---|---|---|
| 1 | 5,000 | +15% | Craft Lv50 |
| 5 | 2,050,312 | +75% | Craft Lv80 |
| 10 | 3,783,403,212 | +150% | Craft Lv130 |

### 42.3 Building Branch

#### T1 — Scaffolding
| Level | Cost 🪙 | Build Speed | Build Req |
|---|---|---|---|
| 1 | 100 | +15% | Build Lv7 |
| 5 | 2,342 | +75% | Build Lv15 |
| 10 | 120,726 | +150% | Build Lv25 |

#### T2 — Mortar Mastery
| Level | Cost 🪙 | Mortar Str Reduction | Build Req |
|---|---|---|---|
| 1 | 200 | -2% | Build Lv13 |
| 5 | 7,812 | -10% | Build Lv25 |
| 10 | 762,939 | -20% (capped) | Build Lv40 |

#### BL3 — Reinforced Joints
| Level | Cost 🪙 | Joint Str | Build Req |
|---|---|---|---|
| 1 | 600 | +10% | Build Lv25 |
| 5 | 48,600 | +50% | Build Lv45 |
| 10 | 11,809,800 | +100% | Build Lv70 |

#### BL4 — Auto-Architect
| Level | Cost 🪙 | Auto-Build Mult | Build Req |
|---|---|---|---|
| 1 | 3,000 | +15% | Build Lv43 |
| 5 | 768,000 | +75% | Build Lv75 |
| 10 | 786,432,000 | +150% | Build Lv115 |

### 42.4 General Branch

#### T5 — Golden Touch
| Level | Cost 🪙 | Gold Mult | General Req |
|---|---|---|---|
| 1 | 300 | +15% | General Lv14 |
| 5 | 24,300 | +75% | General Lv30 |
| 10 | 5,904,900 | +150% | General Lv50 |

#### F1 — Fortress Foundation
| Level | Cost 🪙 | Reinf Mult | General Req |
|---|---|---|---|
| 1 | 500 | +10% | General Lv19 |
| 5 | 75,031 | +50% | General Lv35 |
| 10 | 39,407,819 | +100% | General Lv55 |

#### D1 — Divine Inspiration
| Level | Cost 🪙 | XP Mult | General Req |
|---|---|---|---|
| 1 | 1,000 | +15% | General Lv30 |
| 5 | 256,000 | +75% | General Lv50 |
| 10 | 262,144,000 | +150% | General Lv75 |

#### GE4 — Babel's Blessing
| Level | Cost 🪙 | All Mult | General Req |
|---|---|---|---|
| 1 | 10,000 | +10% | General Lv62 |
| 2 | 50,000 | +20% | General Lv74 |
| 3 | 250,000 | +30% | General Lv86 |
| 4 | 1,250,000 | +40% | General Lv98 |
| 5 | 6,250,000 | +50% | General Lv110 |
| 10 | 19,531,250,000 | +100% | General Lv170 |

---

## 43. Function Dependency Map

### 43.1 Core Loop Call Graph

```
init()
  ├── switchTab() — tab click handlers
  ├── htrStart(fn) — hold-to-repeat binding
  ├── load() — save restore
  │     ├── rC(skill) — recalculate all skill levels
  │     └── Offline progress calc
  ├── initTower() — fresh tower
  ├── rC2() — canvas resize
  ├── updateUI() — full UI refresh
  ├── setInterval(autoTick + runAuto + rechargeBurst + tick)
  ├── setInterval(save)
  └── requestAnimationFrame(draw)
```

### 43.2 Tap Action Call Graph

```
gather(id)
  ├── earnX('gathering', base)
  │     ├── rC('gathering')
  │     ├── rC('general')
  │     ├── updateXPBars()
  │     └── triggerXpOverlay()
  ├── showFeed()
  └── updateUI()

craft(mat)
  ├── earnX('crafting', base) → [same earnX chain]
  ├── showFeed()
  └── updateUI()

tapBuild()
  ├── getStab() (stability calculation)
  ├── earnX('building') → [same earnX chain]
  ├── showFeed()
  ├── checkTowerMs() (milestone check)
  └── updateUI()

buildBurst()
  ├── rechargeBurst()
  ├── getStab()
  ├── getBurstPower/Speed/Cost/Cooldown()
  ├── tapBuild() × power (at speed intervals)
  └── updateUI()

buyUpg(id) / buyTech(id) / buyTalent(id) / buyPrestige(id) / burstBuyUpg(id)
  └── updateUI()

buyMs(skill, index)
  └── updateUI()
```

### 43.3 Automation Call Graph (Every 100ms tick)

```
runAuto()
  ├── getAutoInterval('gather') — check gather interval
  │     └── gF() → gather(gr.id) [if tick matches]
  ├── getAutoInterval('craft') — check craft interval
  │     ├── autoCraft() → select recipe
  │     └── craft(selected) [if tick matches]
  ├── getAutoInterval('build') — check build interval
  │     └── tapBuild() [if tick matches & materials available]
  └── [all talent bonuses applied if applicable]

rechargeBurst()
  └── getBurstCharges() + getBurstCooldown() → replenish charges
```

---

## 44. Full HTML Element ID Reference

### 44.1 Top Bar
| ID | Type | Purpose |
|---|---|---|
| `bar` | div | Top bar container |
| `bar-top` | div | Top bar inner layout |
| `xp-strip` | div | XP bars container |
| `xp-general` | div | General XP bar row |
| `xp-skills` | div | Three skill XP bars container |
| `xpf-x` | div | General XP bar fill |
| `xlv-x` | span | General XP bar level display |
| `xpf-g/c/b` | div | Skill XP bar fills |
| `xlv-g/c/b` | span | Skill XP level displays |
| `xfo-g/c/b` | div | XP overlay fills |
| `xp-g/c/b` | div | Skill XP flex containers |
| `notif` | div | Notification toast |

### 44.2 Build Tab
| ID | Type | Purpose |
|---|---|---|
| `build-pane` | div | Build tab container |
| `bc` | canvas | Tower rendering canvas |
| `build-tap-overlay` | div | Tap zone overlay |
| `build-sub` | span | Build status subtitle |
| `burst-panel` | div | Burst upgrades panel |
| `ttech-panel` | div | Tower tech panel |
| `bhud-name` | div | Tower name display |
| `bhud-progress` | div | Height/width/stability display |
| `bhud-stab` | div | Stability bar container |
| `bhud-stab-fill` | div | Stability bar fill |
| `bhud-action` | div | Action prompt text |
| `bhud-burst` | div | Burst charge status |
| `bhud-row` | div | Row brick dot visualization |

### 44.3 Gather Tab
| ID | Type | Purpose |
|---|---|---|
| `gather-pane` | div | Gather tab container |
| `gather-zone` | div | Gather tap zone |
| `gather-status` | div | Gather auto status |

### 44.4 Craft Tab
| ID | Type | Purpose |
|---|---|---|
| `craft-pane` | div | Craft tab container |
| `craft-zone` | div | Craft tap zone |
| `craft-list` | div | Materials list |

### 44.5 Skills Tab
| ID | Type | Purpose |
|---|---|---|
| `skills-pane` | div | Skills tab container |
| `skills-list` | div | Skill XP display |
| `skills-tap` | div | Skills tap zone |
| `milestones-area` | div | Milestones display |
| `skill-upgs-area` | div | Skill upgrades display |
| `talents-grid` | div | Talent grid display |

### 44.6 Talents Tab
| ID | Type | Purpose |
|---|---|---|
| `talents-pane` | div | Talents tab container |
| `talents-tap` | div | Talents tap zone |

### 44.7 Ascend Tab
| ID | Type | Purpose |
|---|---|---|
| `ascend-pane` | div | Ascend tab container |
| `ascend-tap` | div | Ascend tap zone |
| `pr-upgs-area` | div | Prestige upgrades list |

### 44.8 Options Panel
| ID | Type | Purpose |
|---|---|---|
| `options-panel` | div | Options modal |
| `opt-db` | button | Debug multiplier toggle |
| `opt-ul` | button | Unlimited resources toggle |

---

## 45. Complete CSS Style Reference

### 45.1 Layout System
```css
#game { display:flex; flex-direction:column; width:100vw; height:100dvh; }
#bar { flex-shrink:0; }
#xp-strip { flex-shrink:0; }
#tabs { flex-shrink:0; }
#content { flex:1; position:relative; min-height:0; overflow:hidden; }
.pane { position:absolute; inset:0; display:none; flex-direction:column; overflow-y:auto; }
.pane.on { display:flex; }
```

### 45.2 Color Palette
| Role | Color | Hex |
|---|---|---|
| Background | Near-black | `#0a0604` |
| Surface | Deep brown | `#120a06` |
| Surface lighter | Dark brown | `#150c08` |
| Border | Very dark brown | `#1a0e08` |
| Border lighter | Dark amber | `#2a180e` |
| Primary text | Warm white | `#e8ddd0` |
| Gold text | Gold | `#e8c87a`, `#ffd700` |
| Muted text | Dim brown | `#5a3a2a`, `#6a5a4a`, `#7a5a3a` |
| Gather accent | Red-orange | `#d06040` |
| Craft accent | Green | `#50b050` |
| Build accent | Blue | `#5090d0` |
| General XP | Warm white | `#e0d0c0` |
| Resource | Brown | `#c46a3a` |

### 45.3 Key Dimensions
```css
body { font-size:16px; }
#bar-top h1 { font-size:15px; }
.t { font-size:13px; padding:9px 6px; }
.tz { height:64px; border-radius:8px; }
#build-tap-overlay { height:48px; bottom:90px; }
.xpr { height:14px; gap:4px; }
.xpr .xlb { font-size:9px; width:18px; }
.xpr .xn { font-size:9px; width:58px; }
.xpr .xbarw { height:4px; }
.xpr .xlv { font-size:9px; width:14px; }
.g-res .r { font-size:12px; padding:4px 5px; }
.g-res .r .i { font-size:16px; }
.g-res .r .v { font-size:13px; }
```

### 45.4 Animation Timings
| Animation | Duration | Easing |
|---|---|---|
| XP bar width | 0.3s | ease |
| XP overlay width | 0.4s | ease |
| XP overlay opacity | 0.5s | ease |
| XP overlay fade | 0.5s | ease |
| Feed float | 0.8s | ease |
| Level-up pulse | 0.6s | ease |
| Glow pulse | 2s | ease |
| Shake | 0.5s | ease |
| Row entry scale | 0-400ms | — |
| Flex grow XP bar | 0.3s | ease |

---

## 46. Complete Game Loop — Tick-by-Tick Breakdown

### 46.1 The 100ms Tick
```
Every 100ms:
  1. autoTick()         — (empty, reserved for future)
  2. runAuto()          — automation dispatch
  3. rechargeBurst()    — burst charge recovery
  4. S.tick++           — increment counter
  5. if tick % 5 == 0:  — every 500ms
       updateUI()       — full UI refresh

Every 5,000ms:
  6. save()             — persist to localStorage

Every frame (~16ms @ 60fps):
  7. requestAnimationFrame(draw)
       — canvas tower rendering
       — visual effects (sway, cracks, particles)
```

### 46.2 updateUI() Sub-operations
```
updateUI():
  1. updateResourceDisplay()    — gather pane resource grid
  2. updateCraftDisplay()       — craft pane material list
  3. updateHUD()                — build pane heads-up display
  4. updateSkillsUI()           — skills pane XP bars + milestones
  5. updateTalentGrid()         — talents pane talent cards
  6. updateAscendUI()           — ascend pane prestige upgrades
  7. updateXPBars()             — top bar XP strip
  (all inline in one function)
```

### 46.3 draw() Sub-operations (Canvas)
```
draw():
  1. Resize check (rC2)
  2. Sky gradient (height-dependent)
  3. Stars (20 + rowCount dots)
  4. Ground (dark platform)
  5. Empty state text if no rows
  6. Calculate brick dimensions (bH, bW, gap)
  7. Tower sway (stability-based)
  8. Ground shadow
  9. ctx.save() + translate(sway)
  10. Pillars (left + right side columns)
  11. Brick rendering loop:
        a. Empty (e): subtle outline
        b. Hovering (a): semi-transparent + bob + arrow
        c. Placed (d): brick color + optional cracks
  12. Mortar lines between rows
  13. Height tier decorations (at 20/50/100 tiers)
  14. Collapse particles
  15. ctx.restore()
```

---

## 47. All Game Constants Reference

### 47.1 Numeric Constants
| Constant | Value | Location |
|---|---|---|
| Auto interval cap | 15 levels | `getAutoInterval()` |
| Auto interval min | 100ms | `getAutoInterval()` |
| Auto interval scale | 3000 / (1 + 0.5×lv) | `getAutoInterval()` |
| Burst max taps (base) | 200 | `buildBurst()` (legacy default) |
| Hold-to-repeat rate | 120ms | `htrStart()` |
| Tick interval | 100ms | `setInterval` |
| UI update throttle | 500ms (5 ticks) | `tick % 5 === 0` |
| Save interval | 5,000ms | `setInterval(save, 5000)` |
| Max offline time | 86,400,000ms (24h) | `load()` |
| Offline build cap | 500 rows | `load()` |
| Feed popup duration | 800ms | `showFeed()` |
| Notification duration | 1,500ms | `notif()` |
| Level-up party duration | 600ms | `showCeleb()` |
| XP overlay duration | 1,200ms | `triggerXpOverlay()` |
| Debug multiplier | 10 (ON) / 1 (OFF) | `DB` variable |
| Collapse hazard chance | 5% per brick | `getStab()` |
| Repair factor | 3 (÷) | `towerMsClaimed('repair')` |

### 47.2 XP Curve Constants
```js
xpN(lv) = floor(50 × lv × (1 + 0.12 × lv))
// This is a quadratic curve: 50×lv + 6×lv²
// At Lv1: 56 XP
// At Lv10: 1,100 XP
// At Lv100: 65,000 XP
// At Lv500: 1,525,000 XP
```

### 47.3 Stability Constants
```js
// Base formula components:
baseWidth_contribution = 5 × width
constant_base = 25
reinforce_contribution = 30 × reinforceScore
foundation_contribution = 10 × foundationMult

// Collapse thresholds:
safe_zone = stability ≥ 5%
hazard_zone = 0% < stability < 5%
critical_zone = stability ≤ 0%

// Hazard zone collapse probability:
P(collapse per brick) = 0.05 (base)
P(collapse per brick) = 0.0167 (with repair)
```

---

## 48. Migration & Save Compatibility

### 48.1 State Field Migration History

| Version | Fields Added | Migration Code |
|---|---|---|
| v1 → v2 | `S.tech` | `if(!S.tech)S.tech={}` |
| v2 → v3 | `S.tal` | `if(!S.tal)S.tal={}` |
| v3 → v4 | `S.ms` | `if(!S.ms)S.ms={gathering:0,...}` |
| v4 → v5 | `S.sk.xp/lv` | `if(!S.sk)S.sk={gathering:{xp:0,lv:1},...}` |
| v5 → v6 | `S.tower.rows` | `if(!S.tower.rows)S.tower.rows=[]` |
| v6 → v7 | `S.tower._coll` | `if(S.tower._coll===undefined)S.tower._coll=false` |
| v7 → v8 | `S.tower.lastRowTime` | `if(!S.tower.lastRowTime)S.tower.lastRowTime=0` |
| v8 → v9 | `S._selCraft` | `if(!S._selCraft)S._selCraft=null` |
| v9 → v10 | `S.auto` | `if(!S.auto)S.auto={gather:0,craft:0,build:0}` |
| v10 → v11 | `S.autoCraftTick` | `if(S.autoCraftTick===undefined)S.autoCraftTick=0` |
| v11 → v12 | `S.tower.collapses` | `if(typeof S.tower.collapses!=='number')S.tower.collapses=0` |
| v12 → v13 | `S.stat.tallest/legacy/shards` | `if(typeof S.stat.tallest!=='number')S.stat.tallest=0` etc. |
| v13 → v14 | `S.lastSave` | `if(typeof S.lastSave!=='number')S.lastSave=0` |
| v14 → v15 | `S.pr` | `if(!S.pr)S.pr={}` |
| v15 → v16 | `S.tower.tm` | `if(S.tower.tm===undefined)S.tower.tm=0` |
| v16 → v17 | `S.burst` | `if(!S.burst)S.burst={power:20,speed:50,cost:20,cooldown:20,chrg:1,lchrg:1,last:0}` |

### 48.2 Load Process
```
load():
  1. Read 'babel_save' from localStorage
  2. JSON.parse → Object.assign(S, parsed)
  3. Run all migration checks (16+ fields)
  4. Recalculate all skill XP→levels via rC()
  5. Calculate offline progress (up to 24h)
  6. Return true/false
```

---

## 49. All Possible Notification Messages

| Trigger | Message | Duration |
|---|---|---|
| Upgrade purchased | 🔧 `{name}` Lv.`{n}` | 1.5s |
| Tech purchased | ⬆️ `{name}` | 1.5s |
| Talent purchased | 🏰 `{name}` Lv.`{n}` | 1.5s |
| Prestige purchased | 🏛️ `{name}` Lv.`{n}` | 1.5s |
| Milestone claimed | 🏆 `{title}`! | 1.5s |
| Skill level up | 🎉 (color-coded icon + count) | 1.5s |
| Tower collapse | 💥 TOWER COLLAPSED! +`{legacy}`% +💎`{n}` | 1.5s |
| Tower collapse (no shards) | 💥 TOWER COLLAPSED! +`{legacy}`% | 1.5s |
| Tower milestone | 🏗️ `{bonus}`! | 1.5s |
| Burst no charges | ⏳ No burst charges! Wait `{n}`s | 1.5s |
| Burst too unstable | ⚠️ Tower too unstable! | 1.5s |
| Burst stopped mid | ⚠️ Burst stopped - unstable! | 1.5s |
| No materials | Need materials! | 1.5s |
| Need specific material | Need `{mat}` & mortar! | 1.5s |
| Collapsed tap | 💥 Collapsed! Rebuild? | 1.5s |
| Talent req not met | Need `{skill}` Lv`{n}` | 1.5s |
| Tech already owned | Already owned | 1.5s |
| Shard found (ascend) | 💎 Found a Babel Shard! | 1.5s |
| Insight gained (talents) | ✨ Insight gained! | 1.5s |
| Offline progress | ⚡Offline: gains | 1.5s |
| Save exported | 💾 Save copied! | 1.5s |

---

## 50. Error Handling & Edge Cases

### 50.1 Defensive Checks
```js
// Every critical function checks:
if(!mat) return;                    // craft: missing material
if(!r) return;                      // gather: missing resource  
if(S.tower._coll) return;           // build: collapsed tower
if(burstBusy) return;               // burst: already in progress
if((S.stat.gold||0) < c) return;   // buy: insufficient gold
if((S.stat.shards||0) < c) return;  // prestige: insufficient shards
if(l >= u.L) return;                // upgrade: already maxed
if(msG(skill) !== i) return;        // milestone: wrong index
```

### 50.2 Infinite Loop Protection
```js
// XP level recalculation has a hard cap:
while(x >= xpN(l) && m < 10000) { x -= xpN(l); l++; m++; }
// Maximum 10,000 level-ups per recalculation
```

### 50.3 Number Overflow Protection
```js
fmt(n): // Formats numbers to prevent display overflow
  n ≥ 1e9 → X.XB
  n ≥ 1e6 → X.XM
  n ≥ 1e4 → X.XK
  n < 10 → X.X (1 decimal)
  else → Math.floor(n)
```

### 50.4 Canvas Rendering Edge Cases
```js
// Empty tower:
if(!rows || !rows.length) { fillText('Tap to start!'); return; }

// Partial rows (missing bricks):
const brick = row.bricks[b] || {st:'e'};

// Off-screen culling:
if(y < -rowH || y > h) continue;

// Zero-dimension canvas:
if(cW < 20 || cH < 20) { if(rP || cW < 20) rC2(); return; }
```

---

## 51. Complete HTML Structure

```html
<div id="game">
  <!-- TOP BAR -->
  <div id="bar">
    <div id="bar-top">
      <h1>Babel <span>🗼</span></h1>
      <div class="st">
        <span class="gold">🪙<b id="st-gold">0</b></span>
        <span class="hgt">🏗️<b id="st-hgt">0</b></span>
        <span>🏆Lv<span id="st-ms">0</span></span>
        <span onclick="G.toggleOptions()">⚙️</span>
      </div>
    </div>
  </div>

  <!-- XP STRIP -->
  <div id="xp-strip">
    <div id="xp-general">...</div>
    <div id="xp-skills">...</div>
  </div>

  <!-- TABS -->
  <div id="tabs">
    <button class="t on" data-t="gather">⛏️Gather</button>
    <button class="t" data-t="craft">🔨Craft</button>
    <button class="t" data-t="build">🧱Build</button>
    <button class="t" data-t="skills">📊Skills</button>
    <button class="t" data-t="talents">🏰Talents</button>
    <button class="t" data-t="ascend">⬆️Ascend</button>
  </div>

  <!-- CONTENT (6 panes) -->
  <div id="content">
    <div class="pane on" id="gather-pane">...</div>
    <div class="pane" id="craft-pane">...</div>
    <div class="pane" id="build-pane">...</div>
    <div class="pane" id="skills-pane">...</div>
    <div class="pane" id="talents-pane">...</div>
    <div class="pane" id="ascend-pane">...</div>
  </div>

  <!-- NOTIFICATION TOAST -->
  <div id="notif"></div>
</div>
```

---

## 52. All Event Listeners

| Element | Event | Handler | Phase |
|---|---|---|---|
| `.t[data-t]` | click | `switchTab()` | Bubble |
| `#gather-zone` | mousedown | `htrStart(gather)` | Bubble |
| `#gather-zone` | touchstart | `htrStart(gather)` | Passive |
| `#craft-zone` | mousedown | `htrStart(craft)` | Bubble |
| `#craft-zone` | touchstart | `htrStart(craft)` | Passive |
| `#build-tap-overlay` | mousedown | `htrStart(tapBuild)` | Bubble |
| `#build-tap-overlay` | touchstart | `htrStart(tapBuild)` | Passive |
| `#skills-tap` | mousedown | `htrStart(tapSkills)` | Bubble |
| `#skills-tap` | touchstart | `htrStart(tapSkills)` | Passive |
| `#talents-tap` | mousedown | `htrStart(tapTalents)` | Bubble |
| `#talents-tap` | touchstart | `htrStart(tapTalents)` | Passive |
| canvas (`#bc`) | click | `tapBuild()` | Bubble |
| document | mousedown | `lastTapX/Y = e.clientX/Y` | Bubble |
| document | touchstart | `lastTapX/Y = touch.clientX/Y` | Passive |
| document | mouseup | `htrStop()` | Bubble |
| document | touchend | `htrStop()` | Bubble |
| document | touchcancel | `htrStop()` | Bubble |
| document | keydown | Tab switch (1-6), Space/Enter build | Bubble |

---

## 53. Data Flow Diagrams

### 53.1 Resource → Material → Tower Pipeline
```
🟤 Mud ──┐
🌾 Straw ─┼──→ 🧱 Mud Brick ──┐
💧 Water ─┤                    ├──→ 🗼 Tower
          │    🔥 Fired Brick ─┘
🏖️ Sand ──┼──→ 🧴 Mortar ─────┘
🪨 Gravel ─┘
🪨 Lime ───────→ ⚔️ Reinf Brick ──┐
⛰️ Stone ──┐    🗿 Stone Block ───┤
          └──→ 🏛️ Megalith ──────┘
🧱 Clay ───────→ 🔥 Fired Brick ──┘
```

### 53.2 Gold Flow
```
Gather ───→ 🪙 (base + tap upgrades + milestones)
Craft ────→ 🪙 (tier × tap upgrades + milestones)
Build ────→ 🪙 (random 1-3 + tower ms gold)
Skills ───→ 🪙 (random 0.5-1.5)
Talents ──→ 🪙 (random 1-2 + t5 bonus)
Ascend ───→ 🪙 (random 1-2) or 💎 (rare)
                │
                ▼
         🏪 Upgrade Shop
         ├── Tap upgrades (G1-G4, C1-C4)
         ├── Resource % (R1-R6)
         ├── Auto upgrades (AG1-AB3)
         ├── Skill XP ups (SG1-SB3)
         ├── Burst upgrades (BP-BCH)
         ├── Tech (BW, RF, FD)
         └── Talents (×16)
                │
                ▼
         💎 Prestige (via collapse)
         └── P1-P7 upgrades
```

### 53.3 XP Flow
```
Gather tap ──→ ⛏️ Gather XP ──→ 50% ──→ ⚡ General XP
Craft tap ───→ 🔨 Craft XP ───→ 50% ──→ ⚡ General XP
Build tap ───→ 🧱 Build XP ───→ 50% ──→ ⚡ General XP
Skills tap ──→ ⚡ General XP (100%)

Each skill level → unlocks milestones (Lv5-500)
                → enables talent purchases
                → gates resource/material unlocks
```

---

## 54. Performance Considerations

### 54.1 Canvas Optimization
```js
// Off-screen culling: skip rows outside viewport
const startRow = max(0, rows.length - floor(maxDrawH / rowH));
// Only draws visible rows, not all 500+

// Brick-level culling:
if(bx + bW < 0 || bx > w) continue;  // skip off-screen bricks

// Animation timing:
const animT = min(1, rowAge / 400);  // only first 400ms of animation
if(animT <= 0) continue;              // skip invisible rows
```

### 54.2 UI Throttling
```js
// updateUI() only fires every 5th tick (500ms)
if(S.tick % 5 === 0) updateUI();

// Feed popups auto-remove after 800ms
setTimeout(() => f.remove(), 800);

// Notification auto-dismiss after 1.5s
setTimeout(() => n.classList.remove('sh'), 1500);
```

### 54.3 Memory Management
```js
// Tower row storage: each row is an object with bricks array
// At 500 rows × 50 bricks each = 25,000 brick objects max
// Each brick object: {st:'d', doneT:timestamp} or {st:'e'} or {st:'a', posT:timestamp}
// Approximate memory: ~500KB for a full 500-row tower

// Save serialization: JSON.stringify(S)
// Full state with 500-row tower: ~100-200KB
```

---

## 55. Testing & Validation

### 55.1 JS Validation Command
```bash
node -e "const f=require('fs'),h=f.readFileSync('index.html','utf8');\
const m=h.match(/<script>([\s\S]*?)<\/script>/);\
try{new Function(m[1]);console.log('JS OK')}catch(e){console.log('Error:',e.message)}"
```

### 55.2 Deploy Commands
```bash
# Main branch
git add -A && git commit -m "msg" && git push origin main

# GitHub Pages deploy
git checkout gh-pages && git show main:index.html > index.html \
  && git add index.html && git commit -m "deploy: msg" \
  && git push origin gh-pages -f && git checkout main
```

### 55.3 Key Test Scenarios
| Scenario | Expected Behavior |
|---|---|
| Fresh load | Tower with 1 empty row, starting resources |
| Hold gather | Resources + gold + XP increase per 120ms |
| Craft depletion | Resources consumed, materials produced |
| Burst activation | 20 taps at 50ms, 1 charge consumed, 20🪙 deducted |
| Burst recharge | 1 charge restored every 20s (base) |
| Tower collapse | Shards + legacy awarded, tower reset |
| Prestige buy | Shards deducted, upgrade level increased |
| Offline rejoin | Up to 24h of auto-production calculated |
| Tab switching | Content swaps, auto continues in background |

---

*End of Extended Catalog. Total: ~2,000 lines.*
