<template>
  <div class="postit">
    <v-card class="mx-auto" max-width="344">
      <v-card-text>
        <div>review.content</div>
        <p class="text-h4 text--primary">review.topic.content</p>
        <p>review.like_count</p>
        <div class="text--primary">
          review.created_at
          <br />
          review.score
        </div>
      </v-card-text>
    </v-card>
  </div>
</template>

<script>
export default {
  name: "StickyNote",
  components: {},
  props: {
    review: Object,
  },
}
</script>

<style>
.postit {
  color: black;
  line-height: 1;
  text-align: center;
  /* width: 275px;
  margin: 25px; */
  min-height: 250px;
  max-height: 250px;
  padding-top: 35px;
  position: relative;
  border: 1px solid #e8e8e8;
  border-top: 60px solid #fdfd86;
  /* font-family: "Reenie Beanie"; */
  font-size: 3em;
  border-bottom-right-radius: 60px 5px;
  display: flex;
  background: #ffff88; /* Old browsers */
  background: -moz-linear-gradient(
    -45deg,
    #ffff88 81%,
    #ffff88 82%,
    #ffff88 82%,
    #ffffc6 100%
  ); /* FF3.6+ */
  background: -webkit-gradient(
    linear,
    left top,
    right bottom,
    color-stop(81%, #ffff88),
    color-stop(82%, #ffff88),
    color-stop(82%, #ffff88),
    color-stop(100%, #ffffc6)
  ); /* Chrome,Safari4+ */
  background: -webkit-linear-gradient(
    -45deg,
    #ffff88 81%,
    #ffff88 82%,
    #ffff88 82%,
    #ffffc6 100%
  ); /* Chrome10+,Safari5.1+ */
  background: -o-linear-gradient(
    -45deg,
    #ffff88 81%,
    #ffff88 82%,
    #ffff88 82%,
    #ffffc6 100%
  ); /* Opera 11.10+ */
  background: -ms-linear-gradient(
    -45deg,
    #ffff88 81%,
    #ffff88 82%,
    #ffff88 82%,
    #ffffc6 100%
  ); /* IE10+ */
  background: linear-gradient(
    135deg,
    #ffff88 81%,
    #ffff88 82%,
    #ffff88 82%,
    #ffffc6 100%
  ); /* W3C */
  filter: progid:DXImageTransform.Microsoft.gradient( startColorstr='#ffff88', endColorstr='#ffffc6',GradientType=1 ); /* IE6-9 fallback on horizontal gradient */
}

.postit:after {
  content: "";
  position: absolute;
  z-index: -1;
  right: -0px;
  bottom: 20px;
  width: 200px;
  height: 25px;
  background: rgba(0, 0, 0, 0.2);
  box-shadow: 2px 15px 5px rgba(0, 0, 0, 0.4);
  -moz-transform: matrix(-1, -0.1, 0, 1, 0, 0);
  -webkit-transform: matrix(-1, -0.1, 0, 1, 0, 0);
  -o-transform: matrix(-1, -0.1, 0, 1, 0, 0);
  -ms-transform: matrix(-1, -0.1, 0, 1, 0, 0);
  transform: matrix(-1, -0.1, 0, 1, 0, 0);
}

.rotate {
  /* Safari */
  -webkit-transform: rotate(-10deg);
  /* Firefox */
  -moz-transform: rotate(-10deg);
  /* IE */
  -ms-transform: rotate(-10deg);
  /* Opera */
  -o-transform: rotate(-10deg);
  /* Internet Explorer */
  filter: progid: DXImageTransform.Microsoft.BasicImage(rotation=1);
}
</style>
