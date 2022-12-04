<template>
  <div id="movie-detail">
    <div class="backdrop-bar">
      <div id="backdrop" :style="backdrop"></div>
      <div class="details"></div>
    </div>

    <div class="content d-flex flex-column">
      <div class="info row">
        <div
          class="col-2 offset-2 flex-column align-items-center justify-content-around px-0"
        >
          if
          <img
            :src="`https://image.tmdb.org/t/p/original/${movie?.poster_path}`"
            class="poster"
          />
        </div>
        <div
          class="col-8 d-flex flex-column align-items-start justify-content-end pt-5 pb-5"
        >
          <div class="title d-flex">
            <h1>{{ movie?.title }}</h1>
            <div class="stats d-flex">
              <span>⭐{{ movie?.vote_average }}</span>
              <span class="likes">{{ movie?.like_count }}</span>
              <span @click="favoritePost"
                >좋아요 추가 빼기 함수에요.. {{ movie?.like_count }}</span
              >
            </div>
          </div>
          <div class="tag d-flex">
            <span v-for="genre in movie?.genres" :key="genre.id">
              #{{ genre.name }}
            </span>
            <span v-for="topic in topTopics" :key="topic[1]">
              #{{ topic[1] }}
            </span>
          </div>
          <div class="overview">
            <!-- 줄거리 보기 -->
            {{ movie?.overview }}
          </div>
        </div>
      </div>
      <div class="subtitle row justify-content-center my-5">
        <h2>---------------------- REVIEWS -------------------------</h2>
      </div>
      <div class="review-summary row justify-content-center">
        <div class="row align-items-center justify-content-center">
          <div class="col-5">
            <img
              id="word-cloud"
              class="w-75"
              :src="`http://127.0.0.1:8000/static/WordCloud/movie${movie?.id}.png`"
              alt="word-cloud"
            />
          </div>
          <div class="col-5 offset-1">
            <topic-chart
              :topic-list="movie?.topic_count"
              :review-counts="reviewCounts"
            />
            <!-- <rating-component /> -->
          </div>
        </div>
      </div>

      <h3>{{ username }}리뷰를 남겨주세요!</h3>
      <div class="review-form row justify-content-center">
        <review-form @review-post="getData" />
      </div>

      <div class="reviews row">
        <h1>리뷰</h1>
        <review-card
          v-for="(review, idx) in movie?.reviews"
          :key="`review-${idx}`"
          :review="review"
        />
      </div>
      <h1>게시글</h1>
      <button @click.prevent="changeWM">게시글 작성</button>
      <div class="articles row">
        <article-form v-if="writingMode" @post-article="getData" />
        <article-card
          v-for="(article, idx) in movie?.articles"
          :key="`article-${idx}`"
          :article="article"
          @click.prevent="pushArticle(article.id)"
        />
      </div>
      <!-- end container -->
    </div>
    <!-- end movie-card -->
  </div>
</template>

<script>
import axios from "axios"
// import RatingComponent from "@/components/RatingComponent.vue"
import ReviewCard from "@/components/ReviewCard.vue"
import ArticleCard from "@/components/ArticleCard.vue"
import TopicChart from "../components/TopicChart.vue"
import ReviewForm from "@/components/ReviewForm.vue"
import ArticleForm from "@/components/ArticleForm.vue"

export default {
  name: "MovieDetailView",
  components: { TopicChart, ReviewCard, ArticleCard, ReviewForm, ArticleForm },
  data() {
    return {
      movie: null,
      writingMode: false,
    }
  },
  computed: {
    backdrop() {
      return {
        "--backdrop-Img": `url(https://image.tmdb.org/t/p/original${this.movie?.backdrop_path})`,
      }
    },
    topTopics() {
      let a =
        this.movie?.topic_count.length > 2 ? 2 : this.movie?.topic_count.length
      let b = this.movie?.topic_count.filter((val, idx) => {
        if (idx < a) {
          return true
        } else {
          return false
        }
      })
      return b
    },
    reviewCounts() {
      return this.movie?.reviews.length
    },
  },
  methods: {
    getData() {
      axios({
        method: "get",
        url: `http://127.0.0.1:8000/movies/detail/${this.$route.params.movie_id}/`,
      })
        .then((res) => {
          this.movie = res.data
          this.movie.reviews.reverse()
          this.movie.articles.reverse()
        })
        .catch((error) => {
          console.log(error)
        })
    },
    favoritePost() {
      axios({
        method: "post",
        url: `http://127.0.0.1:8000/movies/favorite/${this.$route.params.movie_id}/`,
        headers: {
          Authorization: this.$store.state.token,
        },
        data: {},
      }).then((res) => {
        console.log(res.data.is_liked)
        if (res.data.is_liked) {
          this.movie.like_count += 1
        } else {
          this.movie.like_count -= 1
        }
      })
    },
    changeWM() {
      this.getData()
      this.writingMode = !this.writingMode
    },
    pushArticle(article_id) {
      this.$router.push({ name: "article", params: { article_id: article_id } })
    },
  },
  created() {
    this.getData()
  },
}
</script>
<style>
@charset "UTF-8";

a {
  text-decoration: none;
  color: #5c7fb8;
}

a:hover {
  text-decoration: underline;
}

#movie-detail {
  color: #a9a8a3;
  width: 100%;
}

#movie-detail .container {
  /* margin: 0 auto; */
  width: 100%;
  height: 800px;
  /* background: #f0f0ed; */
  border-radius: 5px;
  position: relative;
}

#movie-detail .backdrop-bar {
  width: 100%;
  height: 500px;
  margin: 0;
  position: relative;
  overflow: hidden;
  z-index: 1;
  /* border-top-left-radius: 5px;
  border-top-right-radius: 5px; */
}

#movie-detail #backdrop {
  content: "";
  width: 100%;
  height: 100%;
  position: absolute;
  overflow: hidden;
  top: 0;
  left: 0;
  background: rgb(54, 52, 52);
  background: var(--backdrop-Img);
  background-size: cover;
  -webkit-mask-image: -webkit-gradient(
    linear,
    left top,
    left bottom,
    color-stop(0, rgba(0, 0, 0, 1)),
    color-stop(0.35, rgba(0, 0, 0, 1)),
    color-stop(0.5, rgba(0, 0, 0, 1)),
    color-stop(0.65, rgba(0, 0, 0, 1)),
    color-stop(0.85, rgba(0, 0, 0, 0.6)),
    color-stop(1, rgba(0, 0, 0, 0))
  );
  z-index: -1;
  transform: skewY(-2.2deg);
  transform-origin: 0 0;
  -webkit-backface-visibility: hidden;
}

#movie-detail .content .poster {
  z-index: 2;
  width: 200px;
  height: 320px;
}

#movie-detail .content {
  position: absolute;
  top: 480px;
  width: 100%;
}

#movie-detail .content:nth-child(2) > * {
  /* padding-left: 3%; */
}

#movie-detail .content .title {
  color: white;
  font-weight: bolder;
  margin-top: 50px;
  margin-bottom: 15px;
}

#movie-detail .content .likes {
  /* margin-left: 24px; */
}

#movie-detail .content .likes:before {
  content: url("https://s3-us-west-2.amazonaws.com/s.cdpn.io/195612/icon_like.png");
  position: relative;
  top: 2px;
  padding-right: 7px;
}

#movie-detail .overview {
  /* position: absolute;
  top: 700px; */
  margin-bottom: 20px;
  text-align: start;
  width: 70%;

  display: -webkit-box;
  -webkit-line-clamp: 3;
  -webkit-box-orient: vertical;

  height: 100%;
  overflow: hidden;
  text-overflow: ellipsis;
  /* line-height: 170%; */
  font-size: 0.95rem;
}
#movie-detail .stats {
  margin-left: 1rem;
}
#movie-detail .stats span {
  border: 1px solid #fff;
  border-radius: 7px;
  padding: 8px 8px 5px;
  height: 2rem;
  width: 5rem;
  line-height: 100%;
  align-self: center;
  margin-left: 0.5rem;
  justify-self: center;
}

#movie-detail .stats span,
#movie-detail .tag span {
  margin-right: 0.8rem;
  white-space: nowrap;
}

#movie-detail .tag {
  /* margin-block: 2%; */
  padding-block: 2%;
}

#movie-detail .tag span:hover {
  /* background: #ddd; */
  color: #5c7fb8;
}

#movie-detail .avatars {
  margin-top: 23px;
}
#movie-detail .avatars img {
  cursor: pointer;
}
#movie-detail .avatars img:hover {
  opacity: 0.6;
}
#movie-detail .avatars a:hover {
  text-decoration: none;
}

#movie-detail a[data-tooltip] {
  position: relative;
}

#movie-detail a[data-tooltip]::before,
#movie-detail a[data-tooltip]::after {
  position: absolute;
  display: none;
  opacity: 0.85;
}

#movie-detail a[data-tooltip]::before {
  /*
   * using data-tooltip instead of title so we
   * don't have the real tooltip overlapping
   */
  content: attr(data-tooltip);
  background: #000;
  color: #fff;
  font-size: 13px;
  padding: 5px;
  border-radius: 5px;
  /* we don't want the text to wrap */
  white-space: nowrap;
  text-decoration: none;
}

#movie-detail a[data-tooltip]::after {
  width: 0;
  height: 0;
  border: 6px solid transparent;
  content: "";
}

#movie-detail a[data-tooltip]:hover::before,
#movie-detail a[data-tooltip]:hover::after {
  display: block;
}

/** positioning **/
/* top tooltip */
#movie-detail a[data-tooltip][data-placement="top"]::before {
  bottom: 100%;
  left: 0;
  margin-bottom: 40px;
}

#movie-detail a[data-tooltip][data-placement="top"]::after {
  border-top-color: #000;
  border-bottom: none;
  bottom: 50px;
  left: 20px;
  margin-bottom: 4px;
}
</style>
