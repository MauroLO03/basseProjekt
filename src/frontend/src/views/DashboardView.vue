<script setup lang="ts">
import { onMounted } from "vue";
import { useMatchStore } from "../stores/matchStore";

const matchStore = useMatchStore();

onMounted(async () => {
  await matchStore.fetchMatch();
});
</script>

<template>
  <div class="dashboard">
    <h1>Dashboard</h1>

    <pre v-if="matchStore.match">{{ JSON.stringify(matchStore.match, null, 2) }}</pre>

    <div v-if="matchStore.match" class="match-card">
      <h2>{{ matchStore.match.homeTeam }} vs {{ matchStore.match.awayTeam }}</h2>
      <p class="league-tag">League: {{ matchStore.match.league }}</p>

      <div class="row">
        <div class="box">
          <h3>1/X/2</h3>
          <p>Home: {{ matchStore.match.prediction.matchWinner.home }}</p>
          <p>Draw: {{ matchStore.match.prediction.matchWinner.draw }}</p>
          <p>Away: {{ matchStore.match.prediction.matchWinner.away }}</p>
        </div>

        <div class="box">
          <h3>HT/FT</h3>
          <p>H/H: {{ matchStore.match.prediction.halfTimeFullTime.homeHome }}</p>
          <p>H/D: {{ matchStore.match.prediction.halfTimeFullTime.homeDraw }}</p>
          <p>H/A: {{ matchStore.match.prediction.halfTimeFullTime.homeAway }}</p>

          <p>D/H: {{ matchStore.match.prediction.halfTimeFullTime.drawHome }}</p>
          <p>D/D: {{ matchStore.match.prediction.halfTimeFullTime.drawDraw }}</p>
          <p>D/A: {{ matchStore.match.prediction.halfTimeFullTime.drawAway }}</p>

          <p>A/H: {{ matchStore.match.prediction.halfTimeFullTime.awayHome }}</p>
          <p>A/D: {{ matchStore.match.prediction.halfTimeFullTime.awayDraw }}</p>
          <p>A/A: {{ matchStore.match.prediction.halfTimeFullTime.awayAway }}</p>
        </div>

        <div class="box">
          <h3>Goals</h3>
          <div
            v-for="goal in matchStore.match.prediction.goals.overUnder"
            :key="goal.line"
          >
            <p>
              {{ goal.line }}:
              Over {{ goal.over }} /
              Under {{ goal.under }}
            </p>
          </div>
        </div>

        <div class="box">
          <h3>Corners</h3>
          <div
            v-for="corner in matchStore.match.prediction.corners.overUnder"
            :key="corner.line"
          >
            <p>
              {{ corner.line }}:
              Over {{ corner.over }} /
              Under {{ corner.under }}
            </p>
          </div>
        </div>

        <div class="box">
          <h3>Cards</h3>
          <div
            v-for="card in matchStore.match.prediction.cards.overUnder"
            :key="card.line"
          >
            <p>
              {{ card.line }}:
              Over {{ card.over }} /
              Under {{ card.under }}
            </p>
          </div>
        </div>

        <div class="box">
          <h3>BTTS</h3>
          <p>Yes: {{ matchStore.match.prediction.bothTeamsScored.yes }}</p>
          <p>No: {{ matchStore.match.prediction.bothTeamsScored.no }}</p>
        </div>
      </div>
    </div>

    <div v-else>
      <p>Loading prediction...</p>
    </div>
  </div>
</template>

<style scoped>
.dashboard {
  padding: 20px;
}
.league-tag {
  color: #666;
  font-style: italic;
  margin-top: -10px;
  margin-bottom: 20px;
}
.row {
  display: flex;
  gap: 20px;
  flex-wrap: wrap;
}
.box {
  min-width: 170px;
  border: 1px solid #ddd;
  border-radius: 10px;
  padding: 15px;
  background: #f8f8f8;
}
h3 {
  margin-top: 0;
}
</style>