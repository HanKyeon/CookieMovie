<template>
  <div>
    <div class="list flex-column">
      <feed-card
        class="each-row align-items-between"
        v-for="(article, idx) in articleList"
        :key="`article-each-${idx}`"
        :article="article"
      />
    </div>
    <infinite-loading @infinite="infiniteHandler" spinner="waveDots">
      <div
        slot="no-more"
        style="
          color: rgb(102, 102, 102);
          font-size: 14px;
          padding: 10px 0px;
          background: black;
        "
      >
        목록의 끝입니다
      </div>
    </infinite-loading>
  </div>

  <!-- <div class="Feed">
    <feed-card
      v-for="(article, idx) in articles"
      :key="`article-${idx}`"
      :article="article"
    />
  </div> -->
</template>

<script>
import FeedCard from "../components/FeedCard.vue"
import axios from "axios"
import InfiniteLoading from "vue-infinite-loading"
// @ is an alias to /src

export default {
  components: {
    FeedCard,
    InfiniteLoading,
    //a
  },
  name: "FeedView",
  data() {
    return {
      articleList: [],
      pgnum: 0,
    }
  },
  methods: {
    getFeed() {
      axios({
        method: "get",
        url: `http://127.0.0.1:8000/community/feed/${this.pgnum}/`,
        headers: {
          Authorization: this.$store.state.token,
        },
        data: {},
      }).then((res) => {
        console.log(res)
        this.articleList = res.data
        this.pgnum += 1
      })
    },
    infiniteHandler($state) {
      const EACH_LEN = 20
      axios({
        method: "get",
        url: `http://127.0.0.1:8000/community/feed/${this.pgnum}/`,
        headers: {
          Authorization: this.$store.state.token,
        },
        data: {},
      }).then((res) => {
        setTimeout(() => {
          if (res.data.length) {
            this.articleList = this.articleList.concat(res.data)
            $state.loaded()
            this.pgnum += 1
            if (res.data.length / EACH_LEN < 1) {
              $state.complete()
            }
          } else {
            $state.complete()
          }
        }, 1000)
      })
    },
  },
  created() {
    this.getFeed()
  },
}
</script>
