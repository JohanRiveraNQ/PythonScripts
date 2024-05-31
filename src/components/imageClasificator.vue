<template>
  <div class="container">
    <h2>
      Bienvenido a tu clasificador de imágenes
    </h2>
    <input v-model="imageUrl" class="input-field" placeholder="Enter image URL" />
    <button @click="classifyImage" class="classify-button">Classify Image</button>
    <div v-if="imageUrl" class="image-preview">
      <h3 class="preview-title">Image Preview:</h3>
      <img :src="imageUrl" alt="Image Preview" class="preview-image" />
    </div>
    <div v-if="result" class="result-container">
      <h3 class="result-title">Result:</h3>
      <pre class="result-json">{{ result }}</pre>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      imageUrl: '',
      result: null,
    };
  },
  methods: {
    async classifyImage() {
      try {
        const response = await axios.post('http://127.0.0.1:5000/image-page', {
          url: this.imageUrl,
        });
        this.result = response.data;
      } catch (error) {
        console.error("There was an error classifying the image:", error);
      }
    },
  },
};
</script>

<style scoped>
.container {
  max-width: 400px;
  margin: 0 auto;
  padding: 20px;
  border: 1px solid #ccc;
  border-radius: 5px;
  background-color: #f9f9f9;
}

.input-field {
  width: 100%;
  padding: 10px;
  margin-bottom: 10px;
  font-size: 16px;
  border: 1px solid #ccc;
  border-radius: 5px;
}

.classify-button {
  display: block;
  width: 100%;
  padding: 10px;
  background-color: #007bff;
  color: #fff;
  font-size: 16px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

.image-preview {
  margin-top: 20px;
}

.preview-title {
  margin-bottom: 10px;
  font-size: 18px;
}

.preview-image {
  max-width: 100%;
  height: auto;
  border: 1px solid #ccc;
  border-radius: 5px;
}

.result-container {
  margin-top: 20px;
}

.result-title {
  margin-bottom: 10px;
  font-size: 18px;
}

.result-json {
  padding: 10px;
  background-color: #f5f5f5;
  border: 1px solid #ccc;
  border-radius: 5px;
  overflow-x: auto;
}

h2 {
    text-align: center;
  }
</style>
