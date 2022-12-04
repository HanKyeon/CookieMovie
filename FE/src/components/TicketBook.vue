<template>
  <div class="book">
    <h1>sdafasdfasdfasdfsadfafsd</h1>
    <div
      v-for="idx in pageMaxCount"
      :key="`book-page-${idx}`"
      :idx="idx"
      :id="`page-${idx}`"
      class="page no-anim"
    >
      <!-- .side-1 -->
      <div class="side-1">
        <div class="content" style="height: 90%">
          <hr-ticket />
          <hr-ticket />
          <hr-ticket />
          <hr-ticket />
        </div>
      </div>
      <!-- .side-2 -->
      <div class="side-2">
        <div class="content">
          <img
            src="`http://127.0.0.1:8000/static/default_img/ndg.png`"
            alt="asdasdasdasd"
          />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
/* 
<div id="page-2" class="page no-anim">
      <!-- .side-1 -->
      <div class="side-1" id="p3">
        <h1>side1???</h1>
        <hr-ticket />
        <div class="content"></div>
      </div>
      <!-- .side-2 -->
      <div class="side-2" id="p4">
        <div class="content"></div>
      </div>
    </div>
*/
import HrTicket from "./hrTicket.vue"
// import TicketItem from "./TicketItem.vue";
export default {
  name: "TicketBook",
  components: {
    // TicketItem,
    HrTicket,
  },
  props: {
    reviews: Array,
  },
  data() {
    return {
      nowPage: 1,
    }
  },
  computed: {
    pageMaxCount() {
      if (this.reviews) {
        return Math.floor(this.reviews.length / 4) + 1
      } else {
        return 0
      }
    },
  },
  updated() {
    // http://stackoverflow.com/a/23371115/604040
    document.querySelectorAll(".page").forEach((page) => {
      page.addEventListener("click", (event) => {
        event.target.classList.remove("no-anim")
        event.target.classList.toggle("flipped")
        document
          .querySelector(".page > div")
          .addEventListener("click", (event) => {
            event.stopPropagation()
          })
        reorder()
      })
    })
    function reorder() {
      document.querySelectorAll(".book").forEach(function () {
        let pages = document.querySelectorAll(".page")
        let pages_flipped = document.querySelectorAll(".flipped")
        console.log(pages.length)
        console.log(pages_flipped.length)
        pages.forEach((page, i) => {
          page.style.zIndex = pages.length - i
        })
        pages_flipped.forEach((page, i) => {
          page.style.zIndex = i + 1
        })
      })
    }
    reorder()
  },
}
</script>

<style>
/* 
    <div id="page-1" class="page no-anim">
      <!-- .side-1 -->
      <div v-for="idx in pageCount" :key="`page-${idx}`" class="side-1" id="p1">
        <div class="content" style="height: 90%">
          <hr-ticket />
          <hr-ticket />
          <hr-ticket />
          <hr-ticket />
        </div>
      </div>
      <!-- .side-2 -->
      <div class="side-2" id="p2" style="height: 1000px">
        <div class="content">
          <hr-ticket />
          <hr-ticket />
        </div>
      </div>
    </div>
*/
/* .book *,
.book *:before,
.book *:after {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  position: relative;
} */
::-webkit-scrollbar {
  width: 12px;
}
::-webkit-scrollbar-thumb {
  background: rgb(161, 155, 155);
}
::-webkit-scrollbar-track {
  background: transparent;
}

::selection {
  background: #222;
  color: white;
}
::-moz-selection {
  background: #222;
  color: white;
}

.book * {
  /* transform-style: preserve-3d; */
}

.book {
  perspective: 70em;
  /* min-height: 700px; */
  /* height: 80%;
  max-height: 700px;
  width: 1200px; */
  background-image: linear-gradient(
      90deg,
      hsla(30, 40%, 50%, 0.6),
      hsla(30, 40%, 20%, 0.9),
      hsla(30, 40%, 50%, 0.4) 90%
    ),
    url("http://inspirationhut3.inspirationhut.netdna-cdn.com/wp-content/uploads/2012/11/Old-Paper-Texture-3.jpg");
  /* position: absolute;
  top: 0;
  left: 0;
  bottom: 0;
  right: 0; */
  /* margin-block: 5%; */

  border: 3px solid hsla(30, 10%, 20%, 1);
  border-radius: 5px;
  box-shadow: 0 0 150px hsla(170, 0%, 0%, 0.4);
}
.book .content {
  /* display: flex;
  flex-direction: column;
  max-height: 100%; */
}
.book .content #hr-ticket {
  /* flex-grow: 1;
  max-width: 100%;
  min-height: 0; */
  /* font-size: smaller; */
}
.book .content #hr-ticket:hover {
  /* transform: scale(1.05);
  box-shadow: 0px 0px 80px -25px rgba(0, 0, 0, 1);
  transition: all 0.4s;
  z-index: 10; */
}
.page {
  /* height: 100%;
  width: 50%;
  line-height: 1.5;
  border-right: 10px solid transparent;
  position: absolute;
  top: 0;
  right: 0;
  transform-origin: 0 50%;
  transition: 0.8s; */
  /* animation: unflip 0.3s linear; */
}

[class*="side"] {
  /* height: 100%;
  width: 100%;
  position: absolute;
  background-color: hsl(30, 40%, 70%);
  background-image: url("http://inspirationhut3.inspirationhut.netdna-cdn.com/wp-content/uploads/2012/11/Old-Paper-Texture-3.jpg");
  background-size: 100% 100%;
  -webkit-backface-visibility: initial;
  backface-visibility: hidden;
  overflow: none;
  padding: 5% 8%; */
}
.side-1 {
  z-index: 2;
  box-shadow: inset 50px 0 50px rgba(0, 0, 0, 0.5);
  transition: 0.5s;
}
.side-2 {
  transform: rotateY(180deg);
  box-shadow: inset -50px 0 50px rgba(0, 0, 0, 0.5);
}
.flipped > .side-1 {
  box-shadow: inset 300px 0 50px rgba(0, 0, 0, 0.3);
  transition: 0.8s;
  /* opacity: 0; */
}
.flipped > [class*="side"] {
  backface-visibility: hidden;
  pointer-events: auto;
}
.page:after {
  /* width: 100px;
  height: 50px;
  background-color: #555;
  position: absolute;
  top: 0;
  bottom: 0;
  right: -100px;
  margin: auto;
  color: white;
  text-shadow: 0 -1px 0 #222;
  line-height: 50px;
  text-align: center;
  font-family: monospace;
  content: "next-page";
  animation: hide 0.8s linear; */
}
.page.flipped:after {
  /* content: "prev-page";
  transform: rotateY(180deg);
  pointer-events: auto; */
}
/* to hide on flip animation */
/* @keyframes hide {
  0% {
    opacity: 0;
  }
  85% {
    opacity: 0;
  }
  100% {
    opacity: 1;
  }
} */
.flipped {
  transform: rotateY(-180deg);
  pointer-events: none;
  /* display: none; */
  /* animation: flip 0.3s linear;
  animation-fill-mode: forwards; */
}

.no-anim,
.no-anim:after {
  animation: none; /* disable animation when page loads */
}
/* @keyframes flip {
  to {
    transform: rotateY(-180deg);
  }
}
@keyframes unflip {
  from {
    transform: rotateY(-180deg);
  }
  to {
    transform: rotateY(0deg);
  }
} */
</style>
