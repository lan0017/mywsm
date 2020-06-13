import Vue from 'vue';
import Router from 'vue-router';
import Books from './components/Books.vue';
import Ping from './components/Ping.vue';
import Home from './components/Home.vue';
import Result from './components/Result.vue';
import Hello from './components/HelloWorld.vue';
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
      path: '/book',
      name: 'Books',
      component: Books,
    },
    {
      path: '/ping',
      name: 'Ping',
      component: Ping,
    },
    {
      path: '/hello',
      name: 'hello',
      component: Hello,
    },
    {
      path: '/wiki',
      name: 'Wiki',
      component: Wiki,
    },
  ],
});
