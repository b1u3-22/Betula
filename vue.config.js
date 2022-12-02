const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  devServer: {
    allowedHosts: "all",
    proxy: 'http://localhost:5000'
  },
  transpileDependencies: true
})
