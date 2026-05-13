# Monster Generation Data

Use these templates and structures to generate new monsters.

## XML Structure Template

```xml
<?xml version="1.0" encoding="UTF-8"?>
<monster name="Monster Name" nameDescription="a monster description" race="blood/venom/undead/fire/energy" experience="XP" speed="SPEED" manacost="MANA">
	<health now="HP" max="HP" />
	<look type="LOOKTYPE" corpse="CORPSE_ID" />
	<targetchange interval="4000" chance="10" />
	<flags>
		<flag summonable="1" />
		<flag attackable="1" />
		<flag hostile="1" />
		<flag illusionable="1" />
		<flag convinceable="1" />
		<flag pushable="1" />
		<flag canpushitems="0" />
		<flag canpushcreatures="0" />
		<flag targetdistance="1" />
		<flag staticattack="90" />
		<flag runonhealth="0" />
		<flag canwalkonenergy="0" />
		<flag canwalkonfire="0" />
		<flag canwalkonpoison="0" />
	</flags>
	<attacks>
		<attack name="melee" interval="2000" min="MIN" max="MAX" />
		<!-- Optional ranged attacks -->
	</attacks>
	<defenses armor="ARMOR" defense="DEFENSE" />
	<elements>
		<!-- Percent values (positive = resistance, negative = weakness) -->
		<element firePercent="20" />
	</elements>
	<voices interval="5000" chance="10">
		<voice sentence="Sentence 1" />
	</voices>
	<loot>
		<!-- chance: 100000 = 100% -->
		<item name="gold coin" countmax="100" chance="80000" />
	</loot>
</monster>
```

## Base Monster References (Prompt Usage)

When requesting a new monster based on another:
- **Bandit**: Base `Minotaur` (100 HP, Melee 45, Defense 11, Looktype 42)
- **Blacktrunk**: Base `Minotaur Archer` (100 HP, Ranged 80, Defense 6, Looktype 37)
- **Butcher**: Base `Cyclops` (260 HP, Melee High, Looktype 44)

## Registration (monsters.xml)

Always add the monster entry to the correct section in `data/monster/monsters.xml`:
`<monster name="Name" file="Subfolder/file.xml"/>`
