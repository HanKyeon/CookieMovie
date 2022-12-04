<template>
  <div id="topic-chart-bar">
    <div class="cover-gage" :style="gage">
      <p>{{ emoji[topic[1]] }} "{{ topic[1] }}"</p>
    </div>
    <p>{{ topic[0] }}</p>
  </div>
</template>

<script>
export default {
  name: "TopicChartBar",
  props: {
    topic: Array,
    topicLength: Number,
    index: Number,
    reviewCounts: Number,
  },
  data() {
    return {
      emoji: {
        "음악이 좋은": "🎵",
        "영상이 아름다운": "✨",
        "흡입력이 강한": "👀",
        "액션이 통쾌한": "🤸‍♀️",
        "여운이 남는": "💭",
        "인생 최고의": "👍",
        "연기력이 뛰어난": "🎭",
        "스토리가 흥미로운": "🧩",
        "꼭 영화관 가서 봐야하는": "🎬",
        "가슴 설레는": "💘",
        "눈물이 흐르는": "💧",
        "손에 땀을 쥐게 하는": "👋💦",
        "가족과 보기 좋은": "👨‍👩‍👧‍👦",
        "연인과 함께하기 좋은": "💑",
        "혼자 보기 좋은": "🙍‍♂️",
      },
    }
  },
  computed: {
    opacity() {
      return 1 - this.index / this.topicLength
    },
    gage() {
      return {
        background: `rgba(169, 210, 90, ${this.opacity})`,
        width: `${(100 * this.topic[0]) / this.reviewCounts}%`,
      }
    },
  },
}
</script>

<style>
#topic-chart-bar {
  /* background: var(--background); */
  background: rgba(255, 255, 255, 0.5);
  padding-inline: 0px 15px;
  margin: 7px 0;

  overflow: hidden;
  width: 100%;
  border: 1px black;
  border-radius: 10px;
  border-top-right-radius: 10px;
  border-bottom-right-radius: 10px;
  /* color: rgba(0, 0, 0, 0.658); */
  /* padding-inline: 5%; */
  color: rgb(0, 0, 0);
  text-align: center;
  display: flex;
  justify-content: space-between;
}
#topic-chart-bar p {
  font-family: "NanumBarunpen";
  margin-block: 0.5em 0.5em;
  margin-left: 0.5em;
  font-size: 1rem;
  font-weight: bold;
}

#topic-chart-bar p:nth-child(2) {
  /* color: rgb(49, 143, 49); */
  color: black;
}

#topic-chart-bar .cover-gage {
  text-align: center;
  /* background: green top left;
  background-size: 50%; */

  width: 100%;
  height: 100%;
  border-top-right-radius: 10px;
  border-bottom-right-radius: 10px;
  white-space: nowrap;
  overflow: visible;
}
</style>
