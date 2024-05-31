<template>
  <div class="xmen-page">
    <h1 class="xmen-title">X-Men 97</h1>
    <div class="button-container">
      <button class="action-button" @click="consultarXMen">Consultar X-Men</button>
      <button class="action-button" @click="consultarXMenid">Consultar X-Men por id</button>
      <button class="action-button" @click="agregarXMen">Agregar X-Men</button>
      <button class="action-button" @click="eliminarXMen">Eliminar X-Men</button>
      <button class="action-button" @click="actualizarXMen">Actualizar X-Men</button>
      <button class="action-button" @click="imageClasificator">Image Clasificator</button>
    </div>
    <div v-if="mostrarFormulario">
      <!-- Formulario para agregar un nuevo X-Men -->
      <form @submit.prevent="guardarXMen">
        <h2>{{ modoFormulario === 'agregar' ? 'Agregar' : 'Actualizar' }} X-Men</h2>
        <div>
          <label>ID:</label>
          <input v-model.number="xmenSeleccionado.id" type="number" required>
        </div>
        <div>
          <label>Nombre:</label>
          <input v-model="xmenSeleccionado.name" required>
        </div>
        <div>
          <label>Alias:</label>
          <input v-model="xmenSeleccionado.alias" required>
        </div>
        <div>
          <label>Poderes:</label>
          <input v-model="xmenSeleccionado.powers" required>
        </div>
        <div>
          <label>Ciudad:</label>
          <input v-model="xmenSeleccionado.city" required>
        </div>
        <div>
          <label>Primera aparición:</label>
          <input v-model="xmenSeleccionado.first_appearance" required>
        </div>
        <button type="submit">{{ modoFormulario === 'agregar' ? 'Agregar' : 'Actualizar' }}</button>
      </form>
    </div>
    <div v-if="xmenList.length > 0" class="xmen-list">
      <h2>Listado de X-Men:</h2>
      <ul>
        <li v-for="xmen in xmenList" :key="xmen.id">
          <strong>{{ xmen.name }}</strong> - {{ xmen.alias }}<br>
          <span>Poderes: {{ formatPowers(xmen.powers) }}</span><br>
          <span>Ciudad: {{ xmen.city }}</span><br>
          <span>Primera aparición: {{ xmen.first_appearance }}</span>
          <button @click="editarXMen(xmen)">Editar</button>
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      xmenList: [],
      xmenSeleccionado: {
        id: null,
        name: '',
        alias: '',
        powers: '',
        city: '',
        first_appearance: ''
      },
      mostrarFormulario: false,
      modoFormulario: 'agregar' // 'agregar' o 'actualizar'
    };
  },
  methods: {
    async consultarXMen() {
      try {
        const response = await axios.get('http://127.0.0.1:5000/xmen');
        this.xmenList = response.data;
      } catch (error) {
        console.error('Error al obtener los X-Men:', error);
      }
    },
    async guardarXMen() {
  try {
    if (this.modoFormulario === 'agregar') {
      // Verificar si powers es una cadena
      if (typeof this.xmenSeleccionado.powers === 'string') {
        // Convierte los poderes a un array separado por comas
        this.xmenSeleccionado.powers = this.xmenSeleccionado.powers.split(',');
      }

      const response = await axios.post('http://127.0.0.1:5000/xmen', this.xmenSeleccionado);
      this.xmenList.push(response.data);
    } else if (this.modoFormulario === 'actualizar') {
      // Verificar si powers es una cadena
      if (typeof this.xmenSeleccionado.powers === 'string') {
        // Convierte los poderes a un array separado por comas
        this.xmenSeleccionado.powers = this.xmenSeleccionado.powers.split(',');
      }

      const response = await axios.put(`http://127.0.0.1:5000/xmen/${this.xmenSeleccionado.id}`, this.xmenSeleccionado);
      const index = this.xmenList.findIndex(xmen => xmen.id === this.xmenSeleccionado.id);
      if (index !== -1) {
        this.xmenList[index] = response.data;
      }
    }
    this.mostrarFormulario = false;
    this.xmenSeleccionado = {
      id: '',
      name: '',
      alias: '',
      powers: '',
      city: '',
      first_appearance: ''
    };
  } catch (error) {
    console.error('Error al guardar el X-Men:', error);
  }
},

async consultarXMenid() {
  const id = prompt('Ingresa el ID del X-Men que deseas consultar:');
  const xmenId = parseInt(id);
  if (isNaN(xmenId)) {
    alert('Por favor, ingresa un ID válido.');
    return;
  }

  try {
    console.log(`Consultando X-Men con ID: ${xmenId}`);
    const response = await axios.get(`http://127.0.0.1:5000/xmen/${xmenId}`);
    console.log('Respuesta del servidor:', response.data);

    // Asignar los datos recibidos a xmenList para mostrar solo el X-Men consultado
    this.xmenList = [response.data];

  } catch (error) {
    console.error('Error al obtener el X-Men:', error);
  }
},

imageClasificator() {
      
      this.$router.push('/image-page');}
,

async eliminarXMen() {
  const id = prompt('Ingresa el ID del X-Men que deseas eliminar:');
  const xmenId = parseInt(id);
  if (isNaN(xmenId)) {
    alert('Por favor, ingresa un ID válido.');
    return;
  }

  try {
    await axios.delete(`http://127.0.0.1:5000/xmen/${xmenId}`);
    this.xmenList = this.xmenList.filter(item => item.id !== xmenId);
    alert('X-Men eliminado exitosamente.');
  } catch (error) {
    console.error('Error al eliminar el X-Men:', error);
    alert('Ocurrió un error al intentar eliminar el X-Men.');
  }

    },
    editarXMen(xmen) {
      this.xmenSeleccionado = { ...xmen };
      this.mostrarFormulario = true;
      this.modoFormulario = 'actualizar';
    },
    agregarXMen() {
      this.xmenSeleccionado = {
        id: null,
        name: '',
        alias: '',
        powers: '',
        city: '',
        first_appearance: ''
      };
      this.mostrarFormulario = true;
      this.modoFormulario = 'agregar';
    },
    formatPowers(powers) {
      // Verifica si powers es un array, si no, lo convierte a uno
      if (!Array.isArray(powers)) {
        powers = [powers];
      }
      // Retorna los poderes como una cadena separada por comas
      return powers.join(', ');
    }
  }
};
</script>




<style>
/* Estilos CSS */
.xmen-page {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 100vh;
}

.xmen-title {
  font-size: 48px;
  margin-bottom: 30px;
}

.button-container {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.action-button {
  margin: 10px;
  padding: 10px 20px;
  font-size: 18px;
  background-color: #007bff;
  color: #fff;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

.action-button:hover {
  background-color: #0056b3;
}

.xmen-list {
  margin-top: 20px;
}

.xmen-list ul {
  list-style: none;
  padding: 0;
}

.xmen-list li {
  margin-bottom: 20px;
}

form {
  margin-top: 20px;
  width: 50%;
  max-width: 500px;
}

form div {
  margin-bottom: 10px;
}

form label {
  display: block;
  margin-bottom: 5px;
}

form input {
  width: 100%;
  padding: 8px;
  font-size: 16px;
  border: 1px solid #ccc;
  border-radius: 5px;
}

form button {
  padding: 10px 20px;
  font-size: 18px;
  background-color: #007bff;
  color: #fff;
 
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

form button:hover {
  background-color: #0056b3;
}
</style>
