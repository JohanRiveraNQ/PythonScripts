// vue.config.js
const { DefinePlugin } = require('webpack'); // Importa DefinePlugin desde webpack

module.exports = {
  transpileDependencies: true,
  configureWebpack: {
    // Define las características de Vue
    plugins: [
      new DefinePlugin({
        __VUE_PROD_HYDRATION_MISMATCH_DETAILS__: false
      })
    ]
  }
};

// vue.config.js
module.exports = {
  devServer: {
    headers: {
      'X-Content-Type-Options': 'nosniff'
    }
  }
};
