import Vue from 'vue';
import Router from 'vue-router';

import Home from './components/Home.vue';
import Result from './components/Result.vue';

import Wiki from './components/Wiki.vue';

Vue.use(Router);

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home,
    },
    {
      path: '/result',
      name: 'Result',
      component: Result,
    },
    {
      path: '/wiki',
      name: 'Wiki',
      component: Wiki,
    },
  ],
});
