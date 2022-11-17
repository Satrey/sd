const routes = [
  {
    path: "/",
    component: () => import("layouts/MainLayout.vue"),
    children: [{ path: "", component: () => import("pages/IndexPage.vue") }],
  },

  {
    path: "/auth",
    component: () => import("layouts/AuthLayout.vue"),
    children: [{ path: "", component: () => import("pages/AuthPage.vue") }],
  },

  {
    path: "/tasks",
    component: () => import("layouts/MainLayout.vue"),
    children: [{ path: "", component: () => import("pages/TasksPage.vue") }],
  },

  {
    path: "/dispatchers",
    component: () => import("layouts/MainLayout.vue"),
    children: [
      { path: "", component: () => import("pages/DispatchersPage.vue") },
    ],
  },

  {
    path: "/workers",
    component: () => import("layouts/MainLayout.vue"),
    children: [{ path: "", component: () => import("pages/WorkersPage.vue") }],
  },

  {
    path: "/map",
    component: () => import("layouts/MainLayout.vue"),
    children: [{ path: "", component: () => import("pages/MapPage.vue") }],
  },

  // Always leave this as last one,
  // but you can also remove it
  {
    path: "/:catchAll(.*)*",
    component: () => import("pages/ErrorNotFound.vue"),
  },
];

export default routes;
