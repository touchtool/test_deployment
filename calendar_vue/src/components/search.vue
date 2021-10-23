<template>
  <div class="dropdown">
    <input v-if="Object.keys(selectedItem).length === 0" ref="dropdowninput" v-model.trim="inputValue" class="dropdown-input" type="text" placeholder="Search Calendar..." />
    <div v-else @click="resetSelection" class="dropdown-selected">
      {{ selectedItem.name }}
    </div>
    <div v-show="inputValue && apiLoaded" class="dropdown-list">
      <div @click="selectItem(item)" v-show="itemVisible(item)" v-for="item in itemList.calendar" :key="item.name" class="dropdown-item">
        <div style="display:flex; justify-content:space-between">
        <div>{{ item.name }}</div><div>Calendars</div>
        </div>
      </div>
      <div @click="selectItemEvents(item)" v-show="itemVisible(item)" v-for="item in itemList.event" :key="item.name" class="dropdown-item">
        <div style="display:flex; justify-content:space-between">
        <div>{{ item.name }}</div><div>Events</div>
        </div>
      </div>
    </div>
  </div>
</template>


<script>
import axios from 'axios'
import Calendar from '../components/Calendar.vue'
import { globalLocales } from '@fullcalendar/common'

export default {
  data () {
    return {
      selectedItem: {},
      inputValue: '',
      itemList: [],
      apiLoaded: false,
    }
  },
  mounted () {
    this.getList()
  },
  components: {
    Calendar, // make the <FullCalendar> tag available
  },
  methods: {
    resetSelection () {
      this.selectedItem = {}
      this.$nextTick( () => this.$refs.dropdowninput.focus() )
      this.$emit('on-item-reset')
    },
    selectItem (theItem) {
      this.selectedItem = theItem 
      this.inputValue = ''
      this.$emit('on-item-selected', theItem)
      this.$router.push({ path: `/calendar/${theItem.slug}` })
    },
    slice_slug(slug){
      var str = slug;

      var url_calendar = "";
      for(var i =1; i< str.length;i++){
		    url_calendar += str[i];
        if (str[i] == '/'){
          break;
        }
      }
      return url_calendar
    },
    async selectItemEvents (theItem){
      this.selectedItemEvent = theItem 
      this.inputValue = ''
      this.$emit('on-item-selected', theItem)
      // console.log('date', theItem.start_date)
      // console.log('slug=', this.slice_slug(theItem.get_absolute_url))
      await this.$router.push({ path: `/calendar/${this.slice_slug(theItem.get_absolute_url)}` })
      Calendar.components.FullCalendar.calendar.currentData.calendarApi.gotoDate(theItem.start_date)
      let info = Calendar.components.FullCalendar.calendar.currentData.calendarOptions.events
      // for(var i =1; i< str.length;i++){
      //   if (info[i]==theItem.name){
      //     Calendar.methods.handleEventClick(info[i])
      //   }
      // }
      console.log(Calendar.components.FullCalendar.calendar.currentData.calendarOptions.events)
      console.log(theItem)

      // Calendar.methods.handleEventClick()
      // console.log(Calendar.methods.handleEventClick(theItem))
    },
    itemVisible (item) {
      let currentName = item.name.toLowerCase()
      let currentInput = this.inputValue.toLowerCase()
      return currentName.includes(currentInput)
    },
    getList () {
      axios.get('/api/calendar/search').then( response => {
        this.itemList = response.data
        this.apiLoaded = true
      })
    }
  },
  prop: ["modalActive"],
}
</script>

<style>
.dropdown{
  position: relative;
  width: 100%;
  max-width: 400px;
  margin: 0 auto;
}
.dropdown-input, .dropdown-selected{
  width: 100%;
  padding: 10px 16px;
  border: 1px solid transparent;
  background: #edf2f7;
  line-height: 1.5em;
  outline: none;
  border-radius: 8px;
}
.dropdown-input:focus, .dropdown-selected:hover{
  background: #fff;
  border-color: #e2e8f0;
}
.dropdown-input::placeholder{
  opacity: 0.7;
}
.dropdown-selected{
  font-weight: bold;
  cursor: pointer;
}
.dropdown-list{
  position: absolute;
  width: 100%;
  max-height: 500px;
  margin-top: 4px;
  overflow-y: auto;
  background: #ffffff;
  box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05);
  border-radius: 8px;
}
.dropdown-item{
  padding: 11px 16px;
  width: 94%;
  cursor: pointer;
}
.dropdown-item:hover{
  background: #edf2f7;
}
.dropdown-item-flag{
  max-width: 24px;
  max-height: 18px;
  margin: auto 12px auto 0px;
}
</style>
