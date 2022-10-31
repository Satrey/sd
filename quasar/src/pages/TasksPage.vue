<template>
  <q-page class="">
    <div class="q-pa-lg">
      <q-table
        title="Оперативный журнал"
        dense
        :rows="taskStore.taskList"
        :columns="columns"
        row-key="id"
        :pagination="pagination"
        :rows-per-page-options="[0]"
      >
        <template v-slot:body-cell-task_status="props">
          <q-td :props="props">
            <q-checkbox
              v-model="props.row.task_status"
              :color="props.value ? 'green' : 'red'"
              :disable="props.value"
              @click="showAct = !showAct"
            />
          </q-td>
        </template>
        <template v-slot:body-cell-job_doc_number="props">
          <q-td :props="props" class="text-green">
            <div>
                <q-icon class="vertical-middle" style="font-size: 2em;"
                name="picture_as_pdf"
                v-model="props.row.job_doc_number"
                v-if="props.row.job_doc_number"
                :disable="!props.value"
                @click="showAct = !showAct"
             />
            </div>
          </q-td>
        </template>
      </q-table>
      <q-dialog
        v-model="showAct"
        transition-show="scale"
        transition-hide="scale"
        transition-duration="1000"
      >
        <q-card class="bg-white text-black q-px-lg">
          <q-bar>
            <q-icon name="network_wifi" />
            <q-icon name="network_cell" />
            <q-icon name="battery_full" />
            <div>9:34</div>

            <q-space />

            <q-btn dense flat icon="close" v-close-popup>
              <q-tooltip class="bg-white text-primary">Close</q-tooltip>
            </q-btn>
          </q-bar>

          <q-card-section class="q-pt-none" style="width:1000px">
            <br>
            <div v-show="showAct">
              <div class="row text-center">
                <div class="col">
                    <img src="../assets/gerb_tyumen.png" alt="" width="50" height="50">
                </div>
              </div>
              <div class="row text-center">
                <div class="col">МУНИЦИПАЛЬНОЕ КАЗЕННОЕ УЧРЕЖДЕНИЕ</div>
              </div>
              <div class="row text-center">
                <div class="col">«ТЮМЕНЬГОРТРАНС»</div>
              </div>
              <br>
              <div class="row text-center">
                <div class="col">Соблюдай правила техники безопасности!</div>
              </div>
              <br><br>
              <div class="row text-center">
                <div class="col">НАРЯД-ЗАДАНИЕ № {{}}</div>
              </div>
              <div class="row text-center">
                <div class="col">
                  на производство аварийно-восстановительных работ на
                  светофорном объекте
                </div>
              </div>
              <br>
              <div class="row text-right">
                <div class="col">
                  Форма Н-1 (заполняется старшим оператором)
                </div>
              </div>
              <br>
              <div class="row">
                <div class="col">Дата, время поступления заявки:</div>
                <div class="col">19.10.22г. <q-space /> 16-17</div>
              </div>
              <br>
              <div class="row">
                <div class="col">Адрес:</div>
                <div class="col">ул. Пермякова, 71 (пеш)</div>
              </div>
              <br>
              <div class="row">
                <div class="col-4">
                  Замечание,<br />
                  неисправность:
                </div>
                <div class="col-8">не работает кнопка вызова на ТВП</div>
              </div>
              <br>
              <div class="row">
                <div class="col col-4">Передал:</div>
                <div class="col col-8">УДД. т.51-02-76</div>
              </div>
              <br>
              <div class="row">
                <div class="col">Принял ст.оператор: М.М.Буторина</div>
                <div class="col">Подпись</div>
              </div>
              <br>
              <div class="row">
                <div class="col">Наряд выдал: Р.Н.Сырятов</div>
                <div class="col">Подпись</div>
              </div>
              <br>
              <div class="row">
                <div class="col">Наряд направлен для исполнения:</div>
                <div class="col">С.С Сергеев</div>
              </div>
              <br>
              <div class="row">
                <div class="col text-right">
                  Форма Н-2 (заполняется производителем работ)
                </div>
              </div>
              <br>
              <div class="row">
                <div class="col">Наряд получил: С.С Сергеев</div>
                <div class="col">Подпись <hr></div>
              </div>
              <br>
              <div class="row">
                <div class="col">Дата, время прибытия на объект:</div>
                <div class="col">19.10.22г. 16-40</div>
              </div>
              <br>
              <div class="row">
                <div class="col col-4">
                  Обнаруженные <br />
                  недостатки:
                </div>
                <div class="col col-8"></div>
              </div>
              <br>
              <div class="row">
                <div class="col col-4">Выполнено:</div>
                <div class="col col-8">замена кнопки на ТВП — 1шт</div>
              </div>
              <br>
              <div class="row">
                <div class="col">Дата, время устранения недостатков:</div>
                <div class="col">17.10.22г. 16-52</div>
              </div>
              <br>
              <div class="row">
                <div class="col">Дата, время закрытия наряда:</div>
                <div class="col">17.10.22г. 16-52</div>
              </div>
              <br>
              <div class="row">
                <div class="col">Производитель работ: С.С Сергеев</div>
                <div class="col">Подпись</div>
              </div>
              <br>
            </div>
          </q-card-section>
        </q-card>
      </q-dialog>
    </div>
  </q-page>
</template>
  
  <script>
import { defineComponent } from "vue";
import { ref } from "vue";
import { useTaskStore } from "../stores/taskstore";

const columns = [
  {
    name: "number",
    align: "center",
    label: "№",
    field: "number",
    sortable: true,
  },
  {
    name: "dateStart",
    align: "center",
    label: "Время поступления",
    field: (taskList) => taskList.task_start.toLocaleString("ru"),
    sortable: true,
  },
  {
    name: "address",
    required: true,
    label: "Адрес дорожного объекта",
    align: "left",
    field: (taskList) => taskList.address,
    //format: val => `${val}`,
    sortable: true,
  },
  {
    name: "bug_description",
    label: "Описание неисправности",
    field: "bug_description",
    align: "left",
    sortable: true,
  },
  {
    name: "sender",
    label: "Кто передал",
    field: "sender",
    align: "left",
    sortable: true,
  },
  {
    name: "dispatcher",
    label: "Кто принял",
    field: "dispatcher",
    align: "left",
    sortable: true,
  },
  {
    name: "worker",
    label: "Исполнитель",
    field: "worker",
    align: "left",
    sortable: true,
  },
  {
    name: "job_description",
    label: "Выполненные работы",
    field: "job_description",
    align: "left",
    sortable: true,
  },
  {
    name: "job_doc_number",
    label: "Номер документа",
    field: "job_doc_number",
    align: "center",
    sortable: true,
  },
  {
    name: "task_end",
    label: "Время закрытия",
    field: "task_end",
    align: "left",
    sortable: true,
    sort: (a, b) => parseInt(a, 10) - parseInt(b, 10),
  },
  {
    name: "task_status",
    label: "Статус",
    field: "task_status",
    align: "left",
    sortable: true,
  },
];

const taskStore = useTaskStore();

export default defineComponent({
  components: {},
  name: "TasksPage",

  data() {
    return {
      roadObjects: [],
      columns,
      taskStore,
      pagination: ref({
        rowsPerPage: 30,
      }),
      showAct: ref(false),
    };
  },

  computed: {},

  mounted() {
    taskStore.fetchTasks();
  },
});
</script>

<style>
tbody > tr:hover {
  background-color: rgba(0, 60, 95, 0.438);
  color: rgb(255, 255, 255);
  text-shadow: 2px 2px 5px rgba(0, 0, 0, 0.185);
}

.pdf-list {
    width: 800px;
}
</style>

