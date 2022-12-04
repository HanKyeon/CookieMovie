<template>
  <div>
    <div v-if="!onlyUnwatched">
      <div class="list flex-column">
        <movie-card
          class="each-row align-items-between"
          v-for="(movie, idx) in movieList"
          :key="`movie-each-${idx}`"
          :movie="movie"
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
    <div v-if="onlyUnwatched">
      <div class="list flex-column">
        <movie-card
          class="each-row align-items-between"
          v-for="(movie, idx) in movieList"
          :key="`movie-each-${idx}`"
          :movie="movie"
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
  </div>
</template>

<script>
import MovieCard from "./MovieCard.vue"
import axios from "axios"
import InfiniteLoading from "vue-infinite-loading"

export default {
  components: {
    MovieCard,
    InfiniteLoading,
    // a
  },
  name: "MovieList",
  data() {
    return {
      movieList: [],
      negativeMovieList: [],
      limit: 0,
    }
  },
  props: {
    onlyUnwatched: Boolean,
  },
  computed: {
    mode() {
      return this.onlyUnwatched ? "nowatch" : "movie_list"
    },
  },
  methods: {
    getMovies() {
      axios({
        method: "post",
        url: `http://127.0.0.1:8000/movies/${this.mode}/`,
        headers: {
          Authorization: this.$store.state.token,
        },
        data: {
          page: this.limit,
        },
      }).then((res) => {
        this.movieList = res.data
        this.limit += 1
      })
    },
    resetMovies() {
      this.movieList = []
    },
    infiniteHandler($state) {
      const EACH_LEN = 10
      axios({
        method: "post",
        url: `http://127.0.0.1:8000/movies/${this.mode}/`,
        headers: {
          Authorization: this.$store.state.token,
        },
        data: {
          page: this.limit,
        },
      }).then((res) => {
        setTimeout(() => {
          if (res.data.length) {
            this.movieList = this.movieList.concat(res.data)
            $state.loaded()
            this.limit += 1
            console.log("after")
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
  watch: {
    onlyUnwatched() {
      this.limit = 0
      this.resetMovies()
      this.getMovies()
    },
  },
  created() {
    // this.getMovies()
  },
}
</script>

<style>
.list {
  border-radius: 3px;
  overflow: hidden;
  padding: 0% 8% 8% 8%;
}
.list .card {
  /* cursor: pointer; */
  /* min-width: 700px; */
  margin: 4.8% 0% 4.8% 0%;
  padding: 4.5% 4.5% 4.5% 4.5%;
  perspective: 900px;
  transition: all 0.1s;
  background-color: #000;
  box-shadow: 0px 2px 10px rgba(230, 230, 230, 0.2);
  overflow: visible;
  height: 70vh;
}
.list .card .bottom {
  /* height: 0px; */
  overflow: hidden;
  /* width: 200px; */
  font-size: 16px;
  color: #777;
  font-weight: normal;
}
.list .card .open {
  padding: 30px;
  /* height: auto; */
}
.list .card .open .bottom {
  /* margin-top: 10px; */
  /* height: 100%; */
  overflow: visible;
}
.list .card.open .movie-poster-all {
  transform: rotateY(60deg);
  box-shadow: -10px 10px 10px 2px rgba(25, 25, 25, 0.2), -2px 0px 0px 0px #888;
  transition: all 0.5s;
  transition-delay: 0s;
  height: 100%;
  z-index: 10;
}
.list .card.open .info {
  transform: translate(1%, 0%);
  text-align: right;
  text-overflow: hidden;
  width: 50%;
  background: #000 !important;
}
.list .card .info {
  background: #000 !important;
  transform: translate(0%, 0%);
  text-align: right;
  transition: all 0.2s;
  /* min-width: 200px; */
  padding: 1.8% 1.8% 0% 1.8%;
  /* font-family: "Montserrat"; */
  font-weight: bold;
  width: 77%;
}
.list .card.open .members {
  /* padding: 15px 20px; */
  border-radius: 4px;
  align-self: flex-start;
}
.list .card button.simple {
  cursor: pointer;
  color: #ccc;
  border: none;
  outline: none;
  border-radius: 4px;
  background-color: #1ea94b;
  padding: 15px 20px;
  margin: 10px;
  /* font-family: "Montserrat"; */
  font-weight: bold;
  transition: all 0.1s;
}
.list .card button.simple:hover {
  box-shadow: 0px 15px 20px -5px rgba(0, 0, 0, 0.3);
  margin: 10px;
  transform: scale(1.1);
}
.list .card .movie-poster-all {
  transition: all 0.5s;
  /* width: 120px; */
  box-shadow: 0px 2px 10px rgba(0, 0, 0, 0.3);
  overflow: visible;
  height: 100%;
}
.list .card .info .title {
  font-size: 2rem;
  color: #fff;
  letter-spacing: 2px;
}
/*
  .flex-row => movies-flex-row
  .flex-column => movies-flex-column
  .list => .movie-list
  .card => .movies-card
  .bottom => .movies-bottom
  .open => .movies-open
  .bottom => .movies-bottom
  .movie-poster-all => .movies-movie-poster-all
  .info => .movies-info
  .members => .movies-members
  .simple => .movies-simple
  .title => .movies-title
  .group => .movies-group
  .current => .movies-current
  .max => .movies-max
  */
.list .card .info .author {
  font-size: 1rem;
  font-weight: normal;
  color: #888;
  margin-bottom: 8.5px;
}
.list .card .group {
  margin: 0%;
  padding: 5px;
  width: 100%;
  height: 100%;
}
.list .card .members {
  transition: all 0.1s;
  padding: 1%;
  /* font-family: "Montserrat"; */
  color: #ccc;
  background-color: #000;
}
.list .card .members .current {
  /* font-weight: bold; */
  margin-right: 0%;
}
.list .card .members .max {
  opacity: 0.5;
  margin-left: 0%;
}
</style>
