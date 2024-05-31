<template>
  <div class="login">
    <div class="form">
      <h2>X-Men 97</h2>
      <input type="text" placeholder="Username" v-model="username">
      <input type="password" placeholder="Password" v-model="password">
      <input type="submit" value="Sign In" class="submit" @click="signIn">
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      username: '',
      password: '',
      users: [
        { username: 'user1', password: 'password1', secretKey: '123456789' },
        { username: 'user2', password: 'password2', secretKey: '234567891' },
        { username: 'user3', password: 'password3', secretKey: '345678912' }
      ],
      generatedHmac: null 
    };
  },
  methods: {
    signIn() {
      if (!this.username || !this.password) {
        window.alert('Por favor, complete ambos campos.');
        return; 
      }
      const user = this.users.find(user => user.username === this.username && user.password === this.password);
      if (user) {
        this.generateHmac(user.secretKey); 
        this.$router.push('/about');
      } else {
        console.log('Usuario o contraseña incorrectos');
        window.alert('Error: Usuario o contraseña incorrectos');
      }
    },
    generateHmac(secretKey) {
      const secretKeyBuffer = new TextEncoder().encode(secretKey); 
      const contentBuffer = new TextEncoder().encode("Contenido de ejemplo"); 
      crypto.subtle.importKey(
        "raw",
        secretKeyBuffer,
        { name: "HMAC", hash: { name: "SHA-256" } },
        false,
        ["sign"]
      ).then(key => {
        return crypto.subtle.sign(
          "HMAC",
          key,
          contentBuffer
        );
      }).then(signature => {
        const hmacArray = new Uint8Array(signature);
        const generatedHmac = Array.prototype.map.call(hmacArray, x => ('00' + x.toString(16)).slice(-2)).join('');
        console.log("HMAC generado:", generatedHmac);
        this.generatedHmac = generatedHmac; 
      }).catch(err => {
        console.error(err);
      });
    }
  }
};
</script>



<style scoped>
* {
  box-sizing: border-box;
  font-family: sans-serif;
}
.login {
  width: 420px;
  height: 550px;
  border: 1px solid #050505;
  background: url(https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExZXNxNW42aGJpaXBmdzBneW0wZDI0eHpoaDZ6NDhhNjUxeXNuYzUwZiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3og0IV7MOCfnm85iRa/giphy-downsized-large.gif) center center no-repeat;
  background-size: cover;
  margin: 30px auto;
  border-radius: 20px;
}
.login .form {
  width: 100%;
  height: 100%;
  padding: 15px 25px;
}
.login .form h2 {
  color: #FFF;
  text-align: center;
  font-weight: normal;
  font-size: 18px;
  margin-top: 60px;
  margin-bottom: 80px;
}
.login .form input {
  width: 100%;
  height: 40px;
  margin-top: 20px;
  background: rgba(255, 255, 255, .5);
  border: 1px solid rgba(255, 255, 255, .1);
  padding: 0 15px;
  color: #FFF;
  border-radius: 5px;
  font-size: 14px;
}
.login .form input:focus {
  border: 1px solid rgba(255, 255, 255, .8);
  outline: none;
}
::-webkit-input-placeholder {
  color: #DDD;
}
.login .form input.submit {
  background: rgba(255, 255, 255, .9);
  color: #444;
  font-size: 15px;
  margin-top: 40px;
  font-weight: bold;
}
</style>