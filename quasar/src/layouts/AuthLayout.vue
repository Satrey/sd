<template>
  <q-layout view="hHh LpR lFR" class="bg-grey-1">
    <q-header elevated class="bg-white text-grey-8 q-py-xs" height-hint="58">
      <q-toolbar>
        <q-btn
          flat
          dense
          round
          @click="toggleLeftDrawer"
          aria-label="Menu"
          icon="menu"
        />

        <q-btn flat no-caps no-wrap class="q-ml-xs" v-if="$q.screen.gt.xs">
          <img id="org-logo" src="../assets/tt_logo1.png" width="25" />
          <q-toolbar-title id="org-title" shrink class="text-weight-bold">
            <a
              id="site-link"
              href="http://tgt72.ru"
              target="_blank"
              rel="noopener noreferrer"
              >Тюменьгортранс</a
            >
          </q-toolbar-title>
        </q-btn>

        <q-space />

        <div class="q-gutter-sm row items-center no-wrap">
          <q-btn
            round
            dense
            flat
            color="grey-8"
            icon="video_call"
            v-if="$q.screen.gt.sm"
          >
            <q-tooltip>Create a video or post</q-tooltip>
          </q-btn>
          <q-btn
            round
            dense
            flat
            color="grey-8"
            icon="apps"
            v-if="$q.screen.gt.sm"
          >
            <q-tooltip>Apps</q-tooltip>
          </q-btn>
          <q-btn
            round
            dense
            flat
            color="grey-8"
            icon="message"
            v-if="$q.screen.gt.sm"
          >
            <q-tooltip>Messages</q-tooltip>
          </q-btn>
          <q-btn round dense flat color="grey-8" icon="notifications">
            <q-badge color="red" text-color="white" floating> 2 </q-badge>
            <q-tooltip>Notifications</q-tooltip>
          </q-btn>
          <q-btn round flat>
            <q-avatar size="30px">
              <img src="https://cdn.quasar.dev/img/boy-avatar.png" />
            </q-avatar>
            <q-tooltip>Account</q-tooltip>
          </q-btn>
        </div>
      </q-toolbar>
    </q-header>
    <q-page-container>
      <router-view :search="this.search" />
    </q-page-container>
  </q-layout>
</template>

<script>
import { ref } from "vue";

export default {
  name: "MyLayout",

  setup() {
    const leftDrawerOpen = ref(false);
    const search = ref("");

    function toggleLeftDrawer() {
      leftDrawerOpen.value = !leftDrawerOpen.value;
    }

    return {
      leftDrawerOpen,
      search,
      fabRight: ref(true),
      onClick: true,

      toggleLeftDrawer,

      links1: [
        { icon: "home", text: "Оперативный журнал", page_link: "/tasks" },
        { icon: "whatshot", text: "Журнал режимов" },
        { icon: "subscriptions", text: "Журнал отключений" },
      ],
      links2: [
        { icon: "folder", text: "Список объектов", page_link: "/" },
        { icon: "restore", text: "Диспетчера", page_link: "/dispatchers" },
        { icon: "watch_later", text: "Сотрудники", page_link: "/workers" },
        { icon: "thumb_up_alt", text: "Руководство" },
      ],
      links3: [
        { icon: "map", text: "Карта гоода", page_link: "/map" },
        { icon: "local_movies", text: "Movies & Shows" },
        { icon: "videogame_asset", text: "Gaming" },
        { icon: "live_tv", text: "Live" },
      ],
      links4: [
        { icon: "settings", text: "Настройки" },
        { icon: "flag", text: "История" },
        { icon: "help", text: "Помощь" },
        { icon: "feedback", text: "Поддержка" },
      ],
      buttons1: [
        { text: "About" },
        { text: "Press" },
        { text: "Copyright" },
        { text: "Contact us" },
        { text: "Creators" },
        { text: "Advertise" },
        { text: "Developers" },
      ],
    };
  },

  methods: {},

  computed: {},

  mounted() {},
};
</script>

<style lang="css">
body {
  box-sizing: border-box;
}

#org-title {
  text-shadow: 2px 2px 6px rgba(22, 27, 24, 0.363);
  color: rgba(0, 60, 95, 0.849);
}

#site-link {
  text-decoration: none;
  text-shadow: 2px 2px 6px rgba(22, 27, 24, 0.363);
  color: rgba(0, 60, 95, 0.849);
}
</style>

<style lang="sass">
.YL

  &__toolbar-input-container
    min-width: 100px
    width: 55%
    border-radius: 10


  &__toolbar-input-btn
    border-radius: 10
    border-style: solid
    border-width: 1px 1px 1px 0
    border-color: rgba(0,0,0,.24)
    max-width: 60px
    width: 100%

  &__drawer-footer-link
    color: inherit
    text-decoration: none
    font-weight: 500
    font-size: .75rem

    &:hover
      color: #000
</style>
