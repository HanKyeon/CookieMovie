<template>
  <div id="login-page">
    <div
      v-if="!registerActive"
      :class="{ error: emptyFields, container: true }"
    >
      <div class="left">
        <div class="login">Login</div>
        <div class="eula">
          <p>Don't have an account?</p>
          <div class="text-right">
            <a
              href="#"
              @click="
                ;(registerActive = !registerActive), (emptyFields = false)
              "
              >Sign up here</a
            >
          </div>
        </div>
      </div>
      <div class="right">
        <svg viewBox="0 0 320 300">
          <defs>
            <linearGradient
              inkscape:collect="always"
              id="linearGradient"
              x1="13"
              y1="193.49992"
              x2="307"
              y2="193.49992"
              gradientUnits="userSpaceOnUse"
            >
              <stop style="stop-color: #ff00ff" offset="0" id="stop876" />
              <stop style="stop-color: #ff0000" offset="1" id="stop878" />
            </linearGradient>
          </defs>
          <path
            d="m 40,120.00016 239.99984,-3.2e-4 c 0,0 24.99263,0.79932 25.00016,35.00016 0.008,34.20084 -25.00016,35 -25.00016,35 h -239.99984 c 0,-0.0205 -25,4.01348 -25,38.5 0,34.48652 25,38.5 25,38.5 h 215 c 0,0 20,-0.99604 20,-25 0,-24.00396 -20,-25 -20,-25 h -190 c 0,0 -20,1.71033 -20,25 0,24.00396 20,25 20,25 h 168.57143"
          />
        </svg>
        <form class="form" @submit.prevent="doLogin">
          <label for="username">Username</label>
          <input
            type="username"
            id="username"
            v-model="usernameLogin"
            required
          />
          <label for="password">Password</label>
          <input
            type="password"
            id="password"
            v-model="passwordLogin"
            required
          />
          <input type="submit" id="submit" value="Submit" />
        </form>
      </div>
    </div>
    <div v-else :class="{ error: emptyFields, container: true }">
      <div class="left">
        <div class="login">Signup</div>
        <div class="eula">
          <p>Already have an account?</p>
          <div class="text-right">
            <a
              href="#"
              @click="
                ;(registerActive = !registerActive), (emptyFields = false)
              "
              >Sign in here</a
            >
          </div>
        </div>
      </div>
      <div class="right">
        <svg viewBox="0 0 320 300">
          <defs>
            <linearGradient
              inkscape:collect="always"
              id="linearGradient"
              x1="13"
              y1="193.49992"
              x2="307"
              y2="193.49992"
              gradientUnits="userSpaceOnUse"
            >
              <stop style="stop-color: #ff00ff" offset="0" id="stop876" />
              <stop style="stop-color: #ff0000" offset="1" id="stop878" />
            </linearGradient>
          </defs>
          <path
            d="m 40,120.00016 239.99984,-3.2e-4 c 0,0 24.99263,0.79932 25.00016,35.00016 0.008,34.20084 -25.00016,35 -25.00016,35 h -239.99984 c 0,-0.0205 -25,4.01348 -25,38.5 0,34.48652 25,38.5 25,38.5 h 215 c 0,0 20,-0.99604 20,-25 0,-24.00396 -20,-25 -20,-25 h -190 c 0,0 -20,1.71033 -20,25 0,24.00396 20,25 20,25 h 168.57143"
          />
        </svg>
        <form class="form" @submit.prevent="doRegister">
          <label for="username">Username</label>
          <input type="username" id="username" v-model="usernameReg" required />
          <label for="password">Password</label>
          <input type="password" id="password" v-model="passwordReg" required />
          <!-- <input
            v-model="confirmReg"
            type="password"
            class="form-control"
            placeholder="Confirm Password"
            required
          /> -->
          <input
            type="submit"
            id="submit"
            value="Submit"
            @click.prevent="doRegister"
          />
        </form>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios"
import anime from "animejs/lib/anime.es.js"
const URL = "http://127.0.0.1:8000"

export default {
  name: "LoginView",

  methods: {
    doLogin() {
      if (this.usernameLogin === "" || this.passwordLogin === "") {
        this.emptyFields = true
      } else {
        axios({
          method: "post",
          url: `${URL}/accounts/login/`,
          data: {
            username: this.usernameLogin,
            password: this.passwordLogin,
          },
        })
          .then((response) => {
            this.$store.commit("SAVE_TOKEN", response.data.jwt)
            this.$store.commit("SAVE_USERNAME", this.usernameLogin)
            this.$store.dispatch("getUserData", this.usernameLogin)
            this.$router.push({ name: "home" })
          })
          .catch((error) => {
            console.log(error)
          })
      }
    },

    doRegister() {
      if (this.usernameReg === "" || this.passwordReg === "") {
        this.emptyFields = true
      } else {
        axios({
          method: "post",
          url: `${URL}/accounts/signup/`,
          data: {
            username: this.usernameReg,
            password: this.passwordReg,
          },
        })
          .then(() => {
            console.log(this.usernameReg)
            console.log(this.passwordReg)
            this.registerActive = false
          })
          .catch(() => {
            console.log(URL)
          })
      }
    },
  },
  mounted() {
    console.log("mounted")
    var current = null
    console.log(current)

    document.querySelector("#username").addEventListener("focus", function (e) {
      console.log(current)
      console.log(e)
      if (current) current.pause()
      current = anime({
        targets: "path",
        strokeDashoffset: {
          value: 0,
          duration: 700,
          easing: "easeOutQuart",
        },
        strokeDasharray: {
          value: "240 1386",
          duration: 700,
          easing: "easeOutQuart",
        },
      })
      console.log(current)
    })
    document.querySelector("#password").addEventListener("focus", function (e) {
      console.log(e)
      if (current) current.pause()
      current = anime({
        targets: "path",
        strokeDashoffset: {
          value: -336,
          duration: 700,
          easing: "easeOutQuart",
        },
        strokeDasharray: {
          value: "240 1386",
          duration: 700,
          easing: "easeOutQuart",
        },
      })
    })
    document.querySelector("#submit").addEventListener("focus", function (e) {
      console.log(e)
      if (current) current.pause()
      current = anime({
        targets: "path",
        strokeDashoffset: {
          value: -730,
          duration: 700,
          easing: "easeOutQuart",
        },
        strokeDasharray: {
          value: "530 1386",
          duration: 700,
          easing: "easeOutQuart",
        },
      })
    })
  },
  data() {
    return {
      registerActive: false,
      usernameLogin: "",
      passwordLogin: "",
      usernameReg: "",
      passwordReg: "",
      emptyFields: false,
    }
  },
}
</script>

<style>
@import url("https://rsms.me/inter/inter-ui.css");
::selection {
  background: #2d2f36;
}
::-webkit-selection {
  background: #2d2f36;
}
::-moz-selection {
  background: #2d2f36;
}
/* #login-page body {
  background: white;
  font-family: "Inter UI", sans-serif;
  margin: 0;
  padding: 20px;
} */
#login-page {
  display: flex;
  flex-direction: column;
  height: calc(100% - 200px);
  position: absolute;
  place-content: center;
  width: calc(100% - 40px);
  text-align: left;
}
@media (max-width: 767px) {
  #login-page {
    height: auto;
    margin-bottom: 20px;
    padding-bottom: 20px;
  }
}
#login-page .container {
  display: flex;
  height: 320px;
  margin: 0 auto;
  width: 700px;
}
@media (max-width: 767px) {
  #login-page .container {
    flex-direction: column;
    height: 630px;
    width: 320px;
  }
}
#login-page .left {
  background: white;
  color: black;
  height: calc(100% - 40px);
  top: 20px;
  position: relative;
  width: 55%;
}
@media (max-width: 767px) {
  #login-page .left {
    height: 100%;
    left: 20px;
    width: calc(100% - 40px);
    max-height: 270px;
  }
}
#login-page .login {
  font-size: 50px;
  font-weight: 900;
  margin: 50px 40px 40px;
}
#login-page .eula {
  color: #999;
  font-size: 14px;
  line-height: 1.5;
  margin: 40px;
}

#login-page .right {
  background: #474a59;
  box-shadow: 0px 0px 40px 16px rgba(0, 0, 0, 0.22);
  color: #f1f1f2;
  position: relative;
  width: 50%;
}
@media (max-width: 767px) {
  #login-page .right {
    flex-shrink: 0;
    height: 100%;
    width: 100%;
    max-height: 350px;
  }
}
#login-page svg {
  position: absolute;
  width: 320px;
}
#login-page path {
  fill: none;
  stroke: url(#linearGradient);
  stroke-width: 4;
  stroke-dasharray: 240 1386;
}
#login-page .form {
  margin: 40px;
  position: absolute;
}
#login-page label {
  color: #c2c2c5;
  display: block;
  font-size: 14px;
  height: 16px;
  margin-top: 20px;
  margin-bottom: 8px;
}
#login-page input {
  background: transparent;
  border: 0;
  color: #f2f2f2;
  font-size: 20px;
  height: 30px;
  line-height: 30px;
  outline: none !important;
  width: 100%;
}
#login-page input::-moz-focus-inner {
  border: 0;
}
#login-page #submit {
  color: #707075;
  margin-top: 40px;
  transition: color 300ms;
}
#login-page #submit:focus {
  color: #f2f2f2;
}
#login-page #submit:active {
  color: #d0d0d2;
}

/* #login-page {
  display: flex;
  padding: 10%;
  height: 80vh;
  color: black;
}*/

/*#login-page .card {
  padding: 40px 20px;
  background-color: rgb(241, 252, 253);
}
#login-page h1 {
  padding-block: 10px 20px;
}

#login-page .form-group input {
  margin-inline: auto;
  margin-bottom: 20px;
  width: 80%;
}
#login-page .form-group p {
  margin-block: 7% 0;
}

#login-page .wallpaper-login {
  background-size: cover;
  height: 100%;
  position: absolute;
  width: 100%;
}

#login-page .fade-enter-active,
#login-page .fade-leave-active {
  transition: opacity 0.5s;
}
#login-page .fade-enter,
#login-page .fade-leave-to {
  opacity: 0;
}

#login-page .wallpaper-register {
  background-size: cover;
  height: 100%;
  position: absolute;
  width: 100%;
  z-index: -1;
}

#login-page h1 {
  margin-bottom: 1.5rem;
} 

#login-page .error {
  animation-name: errorShake;
  animation-duration: 0.3s;
}

@keyframes errorShake {
  0% {
    transform: translateX(-25px);
  }
  25% {
    transform: translateX(25px);
  }
  50% {
    transform: translateX(-25px);
  }
  75% {
    transform: translateX(25px);
  }
  100% {
    transform: translateX(0);
  }
}*/
</style>
