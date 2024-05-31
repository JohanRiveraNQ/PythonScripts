// src/router/router.js
import { createRouter, createWebHistory } from 'vue-router';
import LoginForm from '@/components/LoginForm.vue';

const routes = [
  {
    path: '/',
    name: 'LoginForm',
    component: LoginForm
  },
  {
    path: '/about',
    name: 'AboutPage',
    component: () => import('../components/AboutPage.vue')
  },
  {
    path: '/hmacgen',
    name: 'HmacGen',
    component: () => import('../components/HmacGen.vue')
  },
  {
    path: '/image-page',
    name: 'imageClasificator',
    component: () => import('../components/imageClasificator.vue')
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;
