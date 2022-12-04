<template>
  <!-- An interactive CSS star rating component.

Has hover and selected states, and could be integrated into a form very easily (as underneath the visual styling it is just radio buttons).  Size and margin between the stars can be easily changed by amending the sass variables.

No JS, all CSS and HTML.

Works on IE9>, Chrome, Firefox, Safari
-->

  <div id="rating">
    <div class="ratingControl">
      <input
        type="radio"
        id="rating-5"
        name="rating"
        value="5"
        :checked="score === 5 ? true : false"
      />
      <label
        class="ratingControl-stars ratingControl-stars--5"
        for="rating-5"
        @click="rate"
        >5</label
      >
      <input
        type="radio"
        id="rating-45"
        name="rating"
        value="4.5"
        :checked="score === 4.5 ? true : false"
      />
      <label
        class="ratingControl-stars ratingControl-stars--45 ratingControl-stars--half"
        for="rating-45"
        @click="rate"
        >45</label
      >
      <input
        type="radio"
        id="rating-4"
        name="rating"
        value="4"
        :checked="score === 4 ? true : false"
      />
      <label
        class="ratingControl-stars ratingControl-stars--4"
        for="rating-4"
        @click="rate"
        >4</label
      >
      <input
        type="radio"
        id="rating-35"
        name="rating"
        value="3.5"
        :checked="score == 3.5 ? true : false"
      />
      <label
        class="ratingControl-stars ratingControl-stars--35 ratingControl-stars--half"
        for="rating-35"
        @click="rate"
        >35</label
      >
      <input
        type="radio"
        id="rating-3"
        name="rating"
        value="3"
        :checked="score === 3 ? true : false"
      />
      <label
        class="ratingControl-stars ratingControl-stars--3"
        for="rating-3"
        @click="rate"
        >3</label
      >
      <input
        type="radio"
        id="rating-25"
        name="rating"
        value="2.5"
        :checked="score === 2.5 ? true : false"
      />
      <label
        class="ratingControl-stars ratingControl-stars--25 ratingControl-stars--half"
        for="rating-25"
        @click="rate"
        >25</label
      >
      <input
        type="radio"
        id="rating-2"
        name="rating"
        value="2"
        :checked="score === 2 ? true : false"
      />
      <label
        class="ratingControl-stars ratingControl-stars--2"
        for="rating-2"
        @click="rate"
        >2</label
      >
      <input
        type="radio"
        id="rating-15"
        name="rating"
        value="1.5"
        :checked="score === 1.5 ? true : false"
      />
      <label
        class="ratingControl-stars ratingControl-stars--15 ratingControl-stars--half"
        for="rating-15"
        @click="rate"
        >15</label
      >
      <input
        type="radio"
        id="rating-1"
        name="rating"
        value="1"
        :checked="score === 1 ? true : false"
      />
      <label
        class="ratingControl-stars ratingControl-stars--1"
        for="rating-1"
        @click="rate"
        >1</label
      >
      <input
        type="radio"
        id="rating-05"
        name="rating"
        value="0.5"
        :checked="score === 0.5 ? true : false"
      />
      <label
        class="ratingControl-stars ratingControl-stars--05 ratingControl-stars--half"
        for="rating-05"
        @click="rate"
        >05</label
      >
    </div>
  </div>
</template>

<script>
export default {
  name: "RatingComponent",
  data() {
    return {
      score: 0,
    }
  },
  props: {
    scoreProp: Number,
  },
  computed: {
    propsScore() {
      return this.scoreProp
    },
  },
  methods: {
    rate(event) {
      this.score = parseFloat(event.target.control.value)
      console.log(this.score)
      this.$emit("score-set", this.score)
    },
    async updateScore() {
      console.log(this.scoreProp)
      console.log(typeof this.scoreProp)
      if (this.scoreProp) {
        this.score = this.scoreProp
      } else {
        console.log("score update failed!")
      }
    },
  },
  created() {
    this.updateScore()
  },
  mounted() {
    this.updateScore()
  },
  // updated() {
  //   this.updateScore()
  // },
}
</script>

<style>
#rating:hover {
  transform: scale(1.2);
  transition: 0.5s;
}
.ratingControl {
  position: relative;
  user-select: none;
  margin: 0 auto;
}
.ratingControl input {
  visibility: hidden;
  /* display: none; */
}

.ratingControl-stars {
  position: absolute;
  top: 0;
  width: 22px;
  height: 22px;
  background-image: url("data:image/svg+xml;charset=US-ASCII,%3C%3Fxml%20version%3D%221.0%22%20encoding%3D%22UTF-8%22%20standalone%3D%22no%22%3F%3E%3Csvg%20width%3D%2215px%22%20height%3D%2214px%22%20viewBox%3D%220%200%2015%2014%22%20version%3D%221.1%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20xmlns%3Axlink%3D%22http%3A%2F%2Fwww.w3.org%2F1999%2Fxlink%22%3E%20%20%20%20%3Ctitle%3EEmpty%20Star%3C%2Ftitle%3E%20%20%20%20%3Cdefs%3E%3C%2Fdefs%3E%20%20%20%20%3Cg%20id%3D%22Page-1%22%20stroke%3D%22none%22%20stroke-width%3D%221%22%20fill%3D%22none%22%20fill-rule%3D%22evenodd%22%3E%20%20%20%20%20%20%20%20%3Cg%20id%3D%22Order-Details---Order-final---Not-reviewed%22%20transform%3D%22translate%28-108.000000%2C%20-385.000000%29%22%20fill%3D%22%23D5D5D5%22%3E%20%20%20%20%20%20%20%20%20%20%20%20%3Cg%20id%3D%22Group%22%20transform%3D%22translate%28108.000000%2C%20316.000000%29%22%3E%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%3Cg%20transform%3D%22translate%280.000000%2C%2069.000000%29%22%20id%3D%22Star-7%22%3E%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%3Cpolygon%20points%3D%227.5%2011.25%203.09161061%2013.5676275%203.93353806%208.65881373%200.367076128%205.18237254%205.2958053%204.46618627%207.5%200%209.7041947%204.46618627%2014.6329239%205.18237254%2011.0664619%208.65881373%2011.9083894%2013.5676275%20%22%3E%3C%2Fpolygon%3E%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%3C%2Fg%3E%20%20%20%20%20%20%20%20%20%20%20%20%3C%2Fg%3E%20%20%20%20%20%20%20%20%3C%2Fg%3E%20%20%20%20%3C%2Fg%3E%3C%2Fsvg%3E");
  background-size: auto 22px;
  background-repeat: no-repeat;
  cursor: pointer;
  text-indent: 100%;
  white-space: nowrap;
  overflow: hidden;
}
.ratingControl-stars:hover,
.ratingControl-stars:hover ~ .ratingControl-stars,
input:checked ~ .ratingControl-stars {
  background-image: url("data:image/svg+xml;charset=US-ASCII,%3C%3Fxml%20version%3D%221.0%22%20encoding%3D%22UTF-8%22%20standalone%3D%22no%22%3F%3E%3Csvg%20width%3D%2215px%22%20height%3D%2214px%22%20viewBox%3D%220%200%2015%2014%22%20version%3D%221.1%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20xmlns%3Axlink%3D%22http%3A%2F%2Fwww.w3.org%2F1999%2Fxlink%22%3E%20%20%20%20%3Ctitle%3ESolid%20Star%3C%2Ftitle%3E%20%20%20%20%3Cdefs%3E%3C%2Fdefs%3E%20%20%20%20%3Cg%20id%3D%22Page-1%22%20stroke%3D%22none%22%20stroke-width%3D%221%22%20fill%3D%22none%22%20fill-rule%3D%22evenodd%22%3E%20%20%20%20%20%20%20%20%3Cg%20id%3D%22Order-Details---Order-final---Not-reviewed%22%20transform%3D%22translate%28-108.000000%2C%20-385.000000%29%22%20fill%3D%22%23FEC844%22%3E%20%20%20%20%20%20%20%20%20%20%20%20%3Cg%20id%3D%22Group%22%20transform%3D%22translate%28108.000000%2C%20316.000000%29%22%3E%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%3Cg%20transform%3D%22translate%280.000000%2C%2069.000000%29%22%20id%3D%22Star-7%22%3E%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%3Cpolygon%20points%3D%227.5%2011.25%203.09161061%2013.5676275%203.93353806%208.65881373%200.367076128%205.18237254%205.2958053%204.46618627%207.5%200%209.7041947%204.46618627%2014.6329239%205.18237254%2011.0664619%208.65881373%2011.9083894%2013.5676275%20%22%3E%3C%2Fpolygon%3E%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%3C%2Fg%3E%20%20%20%20%20%20%20%20%20%20%20%20%3C%2Fg%3E%20%20%20%20%20%20%20%20%3C%2Fg%3E%20%20%20%20%3C%2Fg%3E%3C%2Fsvg%3E");
}
.ratingControl-stars:active,
.ratingControl-stars:active ~ .ratingControl-stars,
input:checked ~ .ratingControl-stars:active {
  background-image: url("data:image/svg+xml;charset=US-ASCII,%3C%3Fxml%20version%3D%221.0%22%20encoding%3D%22UTF-8%22%20standalone%3D%22no%22%3F%3E%3Csvg%20width%3D%2215px%22%20height%3D%2214px%22%20viewBox%3D%220%200%2015%2014%22%20version%3D%221.1%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20xmlns%3Axlink%3D%22http%3A%2F%2Fwww.w3.org%2F1999%2Fxlink%22%3E%20%20%20%20%3Ctitle%3ESolid%20Star%20%E2%80%93%20Light%3C%2Ftitle%3E%20%20%20%20%3Cdefs%3E%3C%2Fdefs%3E%20%20%20%20%3Cg%20id%3D%22Page-1%22%20stroke%3D%22none%22%20stroke-width%3D%221%22%20fill%3D%22none%22%20fill-rule%3D%22evenodd%22%3E%20%20%20%20%20%20%20%20%3Cg%20id%3D%22Order-Details---Order-final---Not-reviewed%22%20transform%3D%22translate%28-108.000000%2C%20-385.000000%29%22%20fill%3D%22%23FFE39C%22%3E%20%20%20%20%20%20%20%20%20%20%20%20%3Cg%20id%3D%22Group%22%20transform%3D%22translate%28108.000000%2C%20316.000000%29%22%3E%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%3Cg%20transform%3D%22translate%280.000000%2C%2069.000000%29%22%20id%3D%22Star-7%22%3E%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%3Cpolygon%20points%3D%227.5%2011.25%203.09161061%2013.5676275%203.93353806%208.65881373%200.367076128%205.18237254%205.2958053%204.46618627%207.5%200%209.7041947%204.46618627%2014.6329239%205.18237254%2011.0664619%208.65881373%2011.9083894%2013.5676275%20%22%3E%3C%2Fpolygon%3E%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%3C%2Fg%3E%20%20%20%20%20%20%20%20%20%20%20%20%3C%2Fg%3E%20%20%20%20%20%20%20%20%3C%2Fg%3E%20%20%20%20%3C%2Fg%3E%3C%2Fsvg%3E");
}

.ratingControl-stars--05 {
  left: 0px;
}

.ratingControl-stars--1 {
  left: 0px;
}

.ratingControl-stars--15 {
  left: 22px;
}

.ratingControl-stars--2 {
  left: 22px;
}

.ratingControl-stars--25 {
  left: 44px;
}

.ratingControl-stars--3 {
  left: 44px;
}

.ratingControl-stars--35 {
  left: 66px;
}

.ratingControl-stars--4 {
  left: 66px;
}

.ratingControl-stars--45 {
  left: 88px;
}

.ratingControl-stars--5 {
  left: 88px;
}

.ratingControl-stars--half {
  width: 11.8px;
}

/* .starpoint_wrap {
  display: inline-block;
}
.starpoint_box {
  position: relative;
  background: url(https://ido-archive.github.io/svc/etc/element/img/sp_star.png)
    0 0 no-repeat;
  font-size: 0;
  line-height: 0em;
}
.starpoint_box .starpoint_bg {
  display: block;
  position: absolute;
  top: 0;
  left: 0;
  height: 18px;
  background: url(https://ido-archive.github.io/svc/etc/element/img/sp_star.png)
    0 -20px no-repeat;
  pointer-events: none;
}
.starpoint_box .label_star {
  margin: 0;
  padding: 0;
  display: inline-block;
  width: 10px;
  height: 18px;
  box-sizing: border-box;
}
.starpoint_box .star_radio {
  opacity: 0;
  width: 0px;
  height: 0px;
  position: absolute;
}
.starpoint_box .star_radio:nth-of-type(1):hover ~ .starpoint_bg,
.starpoint_box .star_radio:nth-of-type(1):checked ~ .starpoint_bg {
  width: 10%;
}
.starpoint_box .star_radio:nth-of-type(2):hover ~ .starpoint_bg,
.starpoint_box .star_radio:nth-of-type(2):checked ~ .starpoint_bg {
  width: 20%;
}
.starpoint_box .star_radio:nth-of-type(3):hover ~ .starpoint_bg,
.starpoint_box .star_radio:nth-of-type(3):checked ~ .starpoint_bg {
  width: 30%;
}
.starpoint_box .star_radio:nth-of-type(4):hover ~ .starpoint_bg,
.starpoint_box .star_radio:nth-of-type(4):checked ~ .starpoint_bg {
  width: 40%;
}
.starpoint_box .star_radio:nth-of-type(5):hover ~ .starpoint_bg,
.starpoint_box .star_radio:nth-of-type(5):checked ~ .starpoint_bg {
  width: 50%;
}
.starpoint_box .star_radio:nth-of-type(6):hover ~ .starpoint_bg,
.starpoint_box .star_radio:nth-of-type(6):checked ~ .starpoint_bg {
  width: 60%;
}
.starpoint_box .star_radio:nth-of-type(7):hover ~ .starpoint_bg,
.starpoint_box .star_radio:nth-of-type(7):checked ~ .starpoint_bg {
  width: 70%;
}
.starpoint_box .star_radio:nth-of-type(8):hover ~ .starpoint_bg,
.starpoint_box .star_radio:nth-of-type(8):checked ~ .starpoint_bg {
  width: 80%;
}
.starpoint_box .star_radio:nth-of-type(9):hover ~ .starpoint_bg,
.starpoint_box .star_radio:nth-of-type(9):checked ~ .starpoint_bg {
  width: 90%;
}
.starpoint_box .star_radio:nth-of-type(10):hover ~ .starpoint_bg,
.starpoint_box .star_radio:nth-of-type(10):checked ~ .starpoint_bg {
  width: 100%;
}

.blind {
  position: absolute;
  clip: rect(0 0 0 0);
  margin: -1px;
  width: 1px;
  height: 1px;
  overflow: hidden;
} */
</style>
