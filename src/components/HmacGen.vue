<template>
    <div>
      <h1>Generador de HMAC</h1>
      <p>Clave secreta: {{ secretKey }}</p>
      <p>HMAC generado: {{ generatedHmac }}</p>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        secretKey: "1234567890",
        generatedHmac: null
      };
    },
    mounted() {
      this.generateHmac();
    },
    methods: {
      generateHmac() {
        // Convertir la clave secreta a un ArrayBuffer
        const secretKeyBuffer = new TextEncoder().encode(this.secretKey);
        // Convertir el contenido de ejemplo a un ArrayBuffer
        const contentBuffer = new TextEncoder().encode(this.exampleContent);
        // Generar el HMAC utilizando la API de crypto del navegador
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
          // Convertir el resultado a una cadena hexadecimal
          const hmacArray = new Uint8Array(signature);
          this.generatedHmac = Array.prototype.map.call(hmacArray, x => ('00' + x.toString(16)).slice(-2)).join('');
          console.log("HMAC generado:", this.generatedHmac);
        }).catch(err => {
          console.error(err);
        });
      }
    }
  };
  </script>
  
  <style scoped>
  /* Estilos específicos del componente */
  </style>
  