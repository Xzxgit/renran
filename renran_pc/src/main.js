// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router/index'
import settings from "./settings"
// elementUI 导入
import ElementUI from 'element-ui';
import "element-ui/lib/theme-chalk/index.css";
// 引入初始化样式
import "../static/css/reset.css";

// 调用插件
Vue.use(ElementUI);

Vue.config.productionTip = false

Vue.prototype.$settings = settings;

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})
