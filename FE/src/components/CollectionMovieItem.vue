<template>
  <b-card
    overlay
    :img-src="`https://image.tmdb.org/t/p/original${movie?.poster_path}`"
    class="m-5 collection-search-item"
    :title="movie?.title"
    text-variant="white"
    style="width: 22%; display: inline-block"
    @click.prevent="toggleMovie"
  >
  </b-card>
</template>

<script>
export default {
  name: "CollectionMovieItem",
  props: {
    movie: Object,
  },
  methods: {
    toggleMovie() {
      this.$emit("toggle-movie", this.movie?.id)
    },
  },
  mounted() {
    let evt = document.createEvent("HTMLEvents")
    evt.initEvent("resize", true, false)
    window.dispatchEvent(evt)
  },
}
</script>

<style>
#bruh {
  width: 1%;
}

#movie-card-in-collection {
  color: black;
}

.collection-search-item:hover {
  transform: scale(1.1);
}
</style>
