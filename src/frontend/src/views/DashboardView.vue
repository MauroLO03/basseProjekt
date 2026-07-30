<script setup lang="ts">
import { onMounted } from "vue";
import { useMatchStore } from "../stores/matchStore";

const matchStore = useMatchStore();

onMounted(async () => {
  await matchStore.fetchMatch(381);
});
</script>

<template>
  <div class="dashboard">
    <h1>Dashboard</h1>

```
<pre v-if="matchStore.match">
  {{ JSON.stringify(matchStore.match, null, 2) }}
</pre>

<div v-if="matchStore.match" class="match-card">

  <h2>
    {{ matchStore.match.homeTeam }}
    vs
    {{ matchStore.match.awayTeam }}
  </h2>

  <p class="league-tag">
    League: {{ matchStore.match.league }}
  </p>


  <div class="row">

    <!-- MATCH WINNER -->
    <div class="box">
      <h3>1/X/2</h3>

      <p>
        Home:
        {{ matchStore.match.prediction.matchWinner.home }}
      </p>

      <p>
        Draw:
        {{ matchStore.match.prediction.matchWinner.draw }}
      </p>

      <p>
        Away:
        {{ matchStore.match.prediction.matchWinner.away }}
      </p>
    </div>


    <!-- HT/FT -->
<div class="box">
  <h3>HT/FT Home</h3>

  <p>
    1/1:
    {{ matchStore.match.prediction.htFtOdds.home.htft_1_1 }}
  </p>

  <p>
    1/X:
    {{ matchStore.match.prediction.htFtOdds.home.htft_1_x }}
  </p>

  <p>
    1/2:
    {{ matchStore.match.prediction.htFtOdds.home.htft_1_2 }}
  </p>

  <p>
    X/1:
    {{ matchStore.match.prediction.htFtOdds.home.htft_x_1 }}
  </p>

  <p>
    X/X:
    {{ matchStore.match.prediction.htFtOdds.home.htft_x_x }}
  </p>

  <p>
    X/2:
    {{ matchStore.match.prediction.htFtOdds.home.htft_x_2 }}
  </p>

  <p>
    2/1:
    {{ matchStore.match.prediction.htFtOdds.home.htft_2_1 }}
  </p>

  <p>
    2/X:
    {{ matchStore.match.prediction.htFtOdds.home.htft_2_x }}
  </p>

  <p>
    2/2:
    {{ matchStore.match.prediction.htFtOdds.home.htft_2_2 }}
  </p>
</div>


<div class="box">
  <h3>HT/FT Away</h3>

  <p>
    H/H:
    {{ matchStore.match.prediction.htFtOdds.away.htft_1_1 }}
  </p>

  <p>
    H/D:
    {{ matchStore.match.prediction.htFtOdds.away.htft_1_x }}
  </p>

  <p>
    H/A:
    {{ matchStore.match.prediction.htFtOdds.away.htft_1_2 }}
  </p>

</div>


    <!-- GOALS -->
    <div class="box">
      <h3>Goals</h3>

      <div
        v-for="goal in matchStore.match.prediction.overUnderOdds.overUnder"
        :key="goal.line"
      >
        <p>
          {{ goal.line }}

          Over:
          {{ goal.over }}

          Under:
          {{ goal.under }}
        </p>
      </div>
    </div>


    <!-- CORNERS -->
    <div class="box">
      <h3>Corners</h3>

      <div
        v-for="corner in matchStore.match.prediction.cornerOdds.overUnder"
        :key="corner.line"
      >
        <p>
          {{ corner.line }}

          Over:
          {{ corner.over }}

          Under:
          {{ corner.under }}
        </p>
      </div>
    </div>


    <!-- CARDS -->
    <div class="box">
      <h3>Yellow Cards</h3>

      <div
        v-for="card in matchStore.match.prediction.yellowCardOdds.overUnder"
        :key="card.line"
      >
        <p>
          {{ card.line }}

          Over:
          {{ card.over }}

          Under:
          {{ card.under }}
        </p>
      </div>
    </div>

  </div>

</div>


<div v-else>
  <p>Loading prediction...</p>
</div>
```

  </div>
</template>

<style scoped>

.dashboard {
  padding:20px;
}


.league-tag {
  color:#666;
  font-style:italic;
}


.row {
  display:flex;
  gap:20px;
  flex-wrap:wrap;
}


.box {
  min-width:200px;
  border:1px solid #ddd;
  border-radius:10px;
  padding:15px;
  background:#f8f8f8;
}


h3 {
  margin-top:0;
}

</style>
