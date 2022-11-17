<template>
  <div class="row items-center" style="height: 100vh">
    <q-space />
    <div class="col-xs-10 col-sm-7 col-md-5 col-lg-4 col-xl-4">
      <q-card class="shadow-14 auth-card">
        <div class="row text-center">
          <q-space />
          <div class="col-10">
            <h4 class="text-center auth-card-text">Авторизация ползователя</h4>
          </div>
          <q-space />
        </div>
        <div class="row q-ma-sm">
          <q-space />
          <q-input class="col-10" v-model="login" outlined label="Логин" />
          <q-space />
        </div>
        <div class="row q-ma-sm">
          <q-space />
          <q-input
            class="col-10"
            v-model="password"
            outlined
            password
            label="Пароль"
            type="password"
          />
          <q-space />
        </div>
        <div class="row col-10 q-ma-sm q-mt-xl">
          <q-space />
          <div class="row">
            <q-space />
            <q-btn
              class="q-ma-sm"
              color="red"
              icon="check"
              label="Отмена"
              @click="onClick"
            />
            <q-btn
              class="q-ma-sm"
              color="primary"
              icon="check"
              label="Принять"
              @click="onClick"
            />
          </div>
          <q-space />
        </div>
      </q-card>
    </div>
    <q-space />
  </div>
</template>

<script>
import { defineComponent } from "vue";
import { ref } from "vue";

export default defineComponent({
  data: () => {
    return {
      login: "",
      password: "",
    };
  },
});
</script>

<style scoped>
.auth-card {
  width: auto;
  height: 400px;
  margin-bottom: 100px;
  border-radius: 10px;
  border-width: 4px;
  border-color: rgba(46, 46, 28, 0.397);
}

.auth-card-text {
  text-shadow: 2px 2px 6px rgba(22, 27, 24, 0.363);
  color: rgba(0, 60, 95, 0.849);
  font-weight: 500;
}
</style>
