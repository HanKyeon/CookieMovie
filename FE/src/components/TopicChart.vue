<template>
  <div id="topic-chart">
    <section>
      <article id="bar_graph">
        <topic-chart-bar
          v-for="(topic, index) in topicList"
          :key="topic[1]"
          :index="index"
          :topic="topic"
          :topic-length="topicList.length"
          :review-counts="reviewCounts"
        ></topic-chart-bar>
      </article>
      <!-- <article id="rerun">
        <p>RERUN</p>
      </article> -->
    </section>
  </div>
</template>

<script>
import TopicChartBar from "./TopicChartBar.vue"
export default {
  name: "TopicChart",
  components: { TopicChartBar },
  props: {
    topicList: Array,
    reviewCounts: Number,
  },
}
</script>

<style>
#topic-chart {
  font-size: 20px;
  text-align: right;
  display: flex;
  align-items: center;
  max-width: 300px;
  max-height: 280px;
  /* border: 1px solid white; */
  padding: 0.8rem 1rem;
  border-radius: 5%;
  background: #ffffff20;
  overflow: auto;
  width: 100%;
}
#topic-chart section {
  display: block;
  margin: 0 auto;
  display: block;
  width: 100%;
}
#topic-chart section #bar_graph {
  /* border-left: 2px solid rgba(255, 255, 255, 0.877); */
}
#topic-chart section #bar_graph #topic:nth-child(2n) {
  animation: grow40 2s forwards ease;
  animation-delay: 0.6s;
}
#topic-chart section #bar_graph #topic:nth-child(3n) {
  animation: grow87 2s forwards ease;
  animation-delay: 0.7s;
}
#topic-chart section #bar_graph #topic:nth-child(4n) {
  animation: grow69 2s forwards ease;
  animation-delay: 0.8s;
}
#topic-chart section #bar_graph #topic p {
  margin: 0;
}
#topic-chart #rerun p {
  padding: 10px 20px;
  border: 2px #fff solid;
  width: max-content;
  display: block;
  margin: 30px auto;
  border-radius: 600px;
  text-align: center;
  color: #fff;
}
#topic-chart #rerun p:hover {
  border: 2px #a9d25a solid;
  color: #676767;
  background: #a9d25a;
}

/* @keyframes grow30 {
  0% {
    width: 0%;
  }
  100% {
    width: 30%;
    padding-right: 10px;
  }
}
@keyframes grow40 {
  0% {
    width: 0%;
  }
  100% {
    width: 40%;
    padding-right: 10px;
  }
}
@keyframes grow87 {
  0% {
    width: 0%;
  }
  100% {
    width: 87%;
    padding-right: 10px;
  }
}
@keyframes grow69 {
  0% {
    width: 0%;
  }
  100% {
    width: 69%;
    padding-right: 10px;
  }
} */
</style>
