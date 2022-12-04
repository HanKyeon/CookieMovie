<template>
  <div id="movie-detail" :style="backdrop">
    <div class="content">
      <div class="movie-info d-flex flex-column justify-content-between">
        <!-- <LazyYoutube
          ref="lazy-trailer"
          :src="`https://www.youtube.com/embed/${movie?.video}`"
        ></LazyYoutube> -->

        <!-- 트레일러 -->
        <div class="trailer" style="visibility: hidden">
          <div class="trailer-ratio">
            <iframe
              id="video"
              autoplay
              frameBorder="0"
              :src="`https://www.youtube.com/embed/${movie?.video}`"
              allow="accelerometer; clipboard-write; encrypted-media; picture-in-picture; gyroscope;"
              class="mx-auto"
            >
            </iframe>
          </div>
        </div>
        <!-- 좌측 기본 정보 -->
        <div class="left-info d-flex flex-column align-items-start">
          <!-- 제목 -->
          <div style="font-size: 4rem; margin-block: 2rem 1rem">
            {{ movie?.title }}
          </div>
          <!-- 별점 -->
          <div style="padding-left: 2rem; scale: 1.5; margin-bottom: 2rem">
            <rating-component
              :score-prop="scoreProp"
              style="display: inline-block"
            />
            <span>{{ movie?.vote_average / 2 }}</span>
          </div>
          <!-- 추천 영화 -->
          <div style="width: 45vw; margin-left: -4%">
            <movie-recommendations />
          </div>
        </div>
      </div>

      <!-- 우측 탭 -->
      <v-row align="center">
        <v-item-group
          v-model="window"
          class="shrink pt-5 align-self-start"
          mandatory
          tag="v-flex"
        >
          <v-item v-for="n in length" :key="n" v-slot="{ active, toggle }">
            <div>
              <v-btn
                :input-value="active"
                icon
                @click="toggle"
                :id="`slot-${n}`"
                color="white"
              >
                <v-icon>mdi-record</v-icon>
              </v-btn>
            </div>
          </v-item>
        </v-item-group>

        <v-col>
          <v-window v-model="window" class="elevation-1" vertical>
            <!-- 첫번째 탭 -->
            <v-window-item key="1">
              <div class="d-flex flex-column p-5">
                <v-row class="mt-0 mb-1">
                  <v-col cols="4" class="align-self-center">
                    <img
                      :src="`https://image.tmdb.org/t/p/original/${movie?.poster_path}`"
                      class="poster"
                      elevation="24"
                      style="border-radius: 10px"
                    />

                    <div id="btn-group" class="d-flex justify-content-around">
                      <v-btn
                        fab
                        small
                        @click="moveToReviewTab"
                        color="amber"
                        backelevation="5"
                        icon
                        ><v-icon> mdi-lead-pencil </v-icon>
                      </v-btn>
                      <v-btn
                        fab
                        small
                        @click="playTrailer"
                        backelevation="5"
                        icon
                        ><v-icon color="grey darken-4">
                          mdi-video-vintage
                        </v-icon>
                      </v-btn>
                      <v-tooltip left color="dark">
                        <template v-slot:activator="{ on, attrs }">
                          <v-btn fab small v-bind="attrs" v-on="on">
                            <v-icon color="teal">mdi-book-plus-multiple</v-icon>
                          </v-btn>
                        </template>
                        <span>컬렉션 만들기</span>
                      </v-tooltip>
                      <v-btn
                        fab
                        small
                        @click="favoritePost"
                        :style="{ color: heartColor }"
                      >
                        <v-icon>mdi-heart</v-icon>
                      </v-btn>
                    </div>
                  </v-col>
                  <v-col
                    cols="8"
                    class="h-100 d-flex flex-column justify-content-center align-items-start"
                  >
                    <h3>
                      {{ movie?.title }}

                      <span style="font-size: 1rem; margin-left: 1rem">{{
                        movie?.release_date.substr(0, 4)
                      }}</span>
                    </h3>
                    <div class="overview paragraph">
                      <!-- 줄거리 -->
                      {{ movie?.overview }}
                    </div>
                    <div class="tag d-flex flex-wrap">
                      <div>
                        <span v-for="genre in movie?.genres" :key="genre.id">
                          #{{ genre.name }}
                        </span>
                      </div>
                      <div>
                        <span v-for="topic in topTopics" :key="topic[1]">
                          #{{ topic[1] }}
                        </span>
                      </div>
                    </div>
                  </v-col>
                </v-row>
                <v-divider></v-divider>
                <!-- 내 리뷰 -->
                <h5
                  style="
                    text-align: start;
                    margin-left: 3rem;
                    margin-top: 1.2rem;
                  "
                >
                  My Review
                </h5>
                <v-row>
                  <v-col cols="10" offset="1" @review-post="getData">
                    <review-form @review-post="getData" />
                  </v-col>
                </v-row>
              </div>
            </v-window-item>
            <!-- 두번째 탭 -->
            <v-window-item key="2" class="">
              <div class="d-flex flex-column align-items-center p-5">
                <div
                  class="review-summary d-flex justify-content-center align-items-center w-100"
                >
                  <v-col cols="5">
                    <topic-chart
                      :topic-list="movie?.topic_count"
                      :review-counts="reviewCounts"
                    />
                  </v-col>
                  <v-col cols="5">
                    <img
                      id="word-cloud"
                      :src="`http://127.0.0.1:8000/static/WordCloud/movie${movie?.id}.png`"
                      alt="word-cloud"
                    />
                  </v-col>

                  <!-- <rating-component /> -->
                </div>
                <br />
                <div
                  class="d-flex justify-content-between align-items-center"
                  style="width: 85%"
                >
                  <v-col cols="5">
                    <h5 style="text-align: start">전체 리뷰 보기</h5>
                  </v-col>
                  <v-col cols="3">
                    <v-select
                      :items="['최신순', '별점순']"
                      label="조회 기준"
                      dense
                      outlined
                      color="white"
                    ></v-select>
                  </v-col>
                </div>
                <div class="reviews d-flex flex-wrap justify-content-center">
                  <review-card
                    v-for="(review, idx) in movie?.reviews"
                    :key="`review-${idx}`"
                    :review="review"
                  />
                </div>
              </div>
            </v-window-item>
            <!-- 세번째 탭 -->
            <v-window-item key="3">
              <div class="d-flex flex-column align-items-center p-5">
                <h3>{{ movie?.title }} 관련 인기 게시글🔥</h3>
                <div class="hot-articles">
                  <v-sheet
                    class="w-100"
                    elevation="20"
                    max-width="800"
                    color="transparent"
                  >
                    <v-slide-group class="pa-3" show-arrows>
                      <v-slide-item
                        v-for="(article, idx) in movie?.articles"
                        :key="`article-${idx}`"
                        v-slot="{ active, toggle }"
                      >
                        <article-card
                          :article="article"
                          class="mx-3 my-3"
                          @click="toggle"
                        >
                          <v-row
                            class="fill-height"
                            align="center"
                            justify="center"
                          >
                            <v-scale-transition>
                              <v-icon
                                v-if="active"
                                color="white"
                                size="48"
                                v-text="'mdi-close-circle-outline'"
                              ></v-icon>
                            </v-scale-transition>
                          </v-row>
                        </article-card>
                      </v-slide-item>
                    </v-slide-group>
                  </v-sheet>
                </div>
                <div class="w-100">
                  <article-form class="m-auto" />
                </div>
              </div>
            </v-window-item>
          </v-window>
        </v-col>
      </v-row>
    </div>
  </div>
</template>

<script>
import axios from "axios"
// import RatingComponent from "@/components/RatingComponent.vue"
import TopicChart from "../components/TopicChart.vue"
import RatingComponent from "../components/RatingComponent.vue"
import MovieRecommendations from "../components/MovieRecommendations.vue"
import ReviewForm from "@/components/ReviewForm.vue"
import ReviewCard from "@/components/ReviewCard.vue"
import ArticleForm from "@/components/ArticleForm.vue"
import ArticleCard from "@/components/ArticleCard.vue"
// import LazyYoutube from "vue-lazytube"

export default {
  name: "MovieDetailView",
  components: {
    TopicChart,
    RatingComponent,
    MovieRecommendations,
    ReviewForm,
    ReviewCard,
    ArticleForm,
    ArticleCard,
  },
  data() {
    return {
      length: 3,
      window: 0,
      movie: null,
      writingMode: false,
      like: false,
    }
  },
  computed: {
    routeMovieId() {
      return this.$route.params.movie_id
    },
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
    heartColor() {
      return this.like ? "#b82a2a" : "lightgray"
    },
    myReview() {
      const myReview = this.movie.reviews.filter((review) => {
        review.writer.username === this.$store.state.username
      })
      return myReview.length ? myReview : null
    },
    scoreProp() {
      return Math.round(this.movie.vote_average) / 2
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
          this.like = this.movie.like_users.some((val) => {
            return val === this.$store.state.userData.id
          })
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
          this.like = true
        } else {
          this.movie.like_count -= 1
          this.like = false
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
    playTrailer() {
      const trailer = document.querySelector(".trailer")
      trailer.style.visibility =
        trailer.style.visibility === "visible" ? "hidden" : "visible"
    },
    moveToReviewTab() {
      this.writingMode = true
      const reviewTab = document.getElementById("slot-1")
      console.log(reviewTab)
      reviewTab.click()
    },
  },
  watch: {
    routeMovieId() {
      this.getData()
    },
  },
  created() {
    this.getData()
  },
  mounted() {
    if (
      this.movie.like_users.some((user) => {
        user === this.$store.state.userData.id
      })
    ) {
      this.like = true
    } else {
      false
    }
  },
  theme: {
    light: false,
  },
}
</script>
<style>
@charset "UTF-8";
a {
  text-decoration: none;
  color: #5c7fb8 !important;
}
#movie-detail {
  /* width: 50vw; */
  /* height: 100%; */
  background: var(--backdrop-Img);
  background-size: cover;
  /* position: fixed; */
  overflow: hidden;
}
#movie-detail .content {
  width: 100%;
  height: 100%;
  backdrop-filter: brightness(60%) blur(1px);
}
#movie-detail .trailer {
  max-width: 650px;
  /* padding: 4rem 1rem 56.25%;
  margin-bottom: 4rem;
  /* padding-bottom: 56.25%; */
  /*height: 0;
  width: 100%;
  position: relative;
  overflow: hidden; */
}

#movie-detail .trailer-ratio {
  height: 0;
  padding-top: 56.25%;
  position: relative;
}
#movie-detail iframe {
  position: absolute;
  top: 50px;
  left: 0;
  width: 100%;
  height: 100%;
}
#movie-detail .trailer object,
#movie-detail .trailer embed {
  /* position: absolute;
  top: -17%;
  left: 0;
  width: 100%;
  height: 100%; */
}

#movie-detail .content .movie-info {
  width: 50vw;
  height: 100vh;
  float: left;
  padding-left: 5vw;
}
#movie-detail .poster {
  width: 80%;
  height: 90%;
  /* height: 320px; */
}
#movie-detail .poster + #btn-group {
  width: 80%;
  margin-inline: auto;
  /* position: absolute;
  bottom: -12%;
  right: 14%; */
}

#movie-detail #btn-group .v-btn {
  background-color: white;
}

#movie-detail .btn {
  color: black;
}
#movie-detail .col-auto {
  padding: 0;
}
#movie-detail .tabs {
  width: 50vw;
  height: 100%;
  float: right;
  overflow: hidden;
}
#movie-detail .movie-info + row {
  width: 50vw;
  height: 100%;
  float: right;
  overflow: hidden;
}

#movie-detail .nav-item {
  margin-block: 0.5rem;
  border: 1px;
  width: 2vw;
}
#movie-detail .nav-tabs {
  border-bottom: 0;
}
#movie-detail .nav-tabs .nav-link {
  border-top-right-radius: 0;
  border-bottom-left-radius: 0.25rem;
  border: 1px solid white;
  border-right: 1px solid transparent;
  padding-inline: 0.5rem;
}
#movie-detail .tab-content {
  background: rgba(37, 35, 35, 0.5);
  position: relative;
  overflow-y: auto;
  height: 100vh;
  /* padding: 2rem 2rem 1rem 2rem; */
}
#movie-detail .v-window-item {
  background: rgba(37, 35, 35, 0.5);
  position: relative;
  overflow-y: auto;
  height: 100vh;
  /* padding: 2rem 2rem 1rem 2rem; */
}
#movie-detail .tab-content .tab-pane {
  padding: 2rem;
}
#movie-detail .overview {
  margin-block: 20px;
  text-align: start;
  width: 100%;
  font-size: 0.92rem;
  /* display: -webkit-box;
  -webkit-line-clamp: 3;
  -webkit-box-orient: vertical;

  overflow: hidden;
  text-overflow: ellipsis;
  font-size: 0.95rem; */
}
#movie-detail .stats {
  /* margin-left: 1rem; */
}
#movie-detail .stats span {
  border: 1px solid #fff;
  border-radius: 7px;
  padding: 8px 8px 5px;
  /* height: 2rem; */
  width: 5rem;
  line-height: 100%;
  align-self: center;
  justify-self: center;
}

#movie-detail #word-cloud {
  max-height: 280px;
  max-width: 300px;
  width: 100%;
  backdrop-filter: opacity(0.5);
}

#movie-detail .reviews {
  backdrop-filter: brightness(300%);
  width: 85%;
  border-radius: 10px;
}
#movie-detail .content .likes:before {
  content: url("https://s3-us-west-2.amazonaws.com/s.cdpn.io/195612/icon_like.png");
  position: relative;
  top: 1px;
  scale: 2;
  /* scale: ; */
  padding-right: 7px;
}
#movie-detail .left-info {
  height: 50%;
}
#movie-detail .left-info .title {
  margin-block: 1vh;
}
#movie-detail .stats span,
#movie-detail .tag span {
  margin-right: 0.8rem;
  white-space: nowrap;
}

#movie-detail .tag {
  margin-top: 2vh;
  /* padding-block: 2%; */
  width: 100%;
}

#movie-detail .tag span:hover {
  /* background: #ddd; */
  color: #5c7fb8;
}

#movie-detail .v-slide-group__prev,
#movie-detail .v-slide-group__next {
  min-width: 5%;
}

#movie-detail .hot-articles {
  max-width: 100%;
}

#movie-detail .v-text-field.v-text-field--enclosed .v-text-field__details {
  margin-bottom: 0;
}
</style>
