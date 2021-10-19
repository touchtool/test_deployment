<script>
import FullCalendar from "@fullcalendar/vue3";
import dayGridPlugin from "@fullcalendar/daygrid";
import timeGridPlugin from "@fullcalendar/timegrid";
import interactionPlugin from "@fullcalendar/interaction";
import EventDetails from './EventDetails'
import {ref} from 'vue'


import axios from 'axios'

export default {
  components: {
    FullCalendar, // make the <FullCalendar> tag available
  },
  data: function () {
    return {
      calendarOptions: {
        timeZone: "UTC",
        plugins: [
          dayGridPlugin,
          timeGridPlugin,
          interactionPlugin, // needed for dateClick
        ],
        headerToolbar: {
          left: "prev,next today",
          center: "title",
          right: "dayGridMonth", //,timeGridWeek,timeGridDay
        },
        initialView: "dayGridMonth",
        // initialEvents: INITIAL_EVENTS,
        events: [],
        // editable: true,
        // selectable: true,
        selectMirror: true,
        dayMaxEvents: true,
        weekends: true,
        // select: this.handleDateSelect,
        eventClick: this.handleEventClick,
        eventsSet: this.handleEvents,
        /* you can update a remote database when these fire:
        eventAdd:
        eventChange:
        eventRemove:
        */
      },
      currentEvents: [],
      calendar_events: [],
      event_details: [],
      modalActive: false,
    };
  },
  setup() {  //EventDetails
  let modalActive = ref(false);
  return {modalActive};
  },
  mounted() {
    this.getCalendarEvents()
  },
  methods: {
    setCalendarEvents(data){
      let d = data
      this.calendar_events = d
      for(let i=0; i<d.length; i++) {
        this.calendarOptions.events.push({
          id: d[i].id,
          title: d[i].name,
          start: d[i].start_date,
          end: d[i].end_date,
          description: d[i].description
        })
        // console.log(this.calendarOptions.events[i])
      }
    },
    getCalendarEvents() {
      const calendar_slug = this.$route.params.calendar_slug
      console.log("slug =", calendar_slug)

      axios
        .get(`/api/calendar/${calendar_slug}`)
        .then(response => {
          this.setCalendarEvents(response.data)
        })
        .catch(error => {
          console.log(error)
        })
    },
    handleWeekendsToggle() {
      this.calendarOptions.weekends = !this.calendarOptions.weekends; // update a property
    },
    handleDateSelect(selectInfo) {
      let title = prompt("Please enter a new title for your event"); //input the title name of event
      let calendarApi = selectInfo.view.calendar;
      calendarApi.unselect(); // clear date selection
      if (title) {
        // if use fill the input
        calendarApi.addEvent(
          {
          id: createEventId(),
          title,
          start: selectInfo.startStr,
          end: selectInfo.endStr,
          allDay: selectInfo.allDay,
          //color: 'red',
          //textColor: 'black',
        });
      }
    },
    handleEventClick(clickInfo) {
      const calendar_slug = this.$route.params.calendar_slug
        this.modalActive = true;
        let event_slug  = clickInfo.event.title.toLowerCase().split(" ").join("-")
        axios
          .get(`/api/calendar/${calendar_slug}/${event_slug}`)
          .then(response => {
            this.event_details = [
              response.data.name,
              response.data.start_date,
              response.data.end_date,
              response.data.description
            ]
          })
          .catch(error => {
            console.log(error)
          })
    },
    handleEvents(events) {
      this.currentEvents = events;
    },
  },
};
</script>
<template>

<div class="ALL">
  <!--Details-->


  <div class="demo-app">
    <div class="demo-app-main">
  <div class='demo-app-sidebar-section'>


  <EventDetails v-show:modalActive="modalActive">
      <div class="modal-content">

        <!-- waiting for fix--- -->
        <h1>gap</h1>
        <h1>gap</h1>
        <!-- waiting for fix--- -->

        <h1>{{ event_details[0] }}</h1>
        <p>start date: {{ event_details[1] }}</p>
          <p>end date:{{ event_details[2] }}</p>
            <p>description:{{ event_details[3] }}</p>
          <button @click="this.modalActive = !this.modalActive"  type="button" name="button">X</button>
      </div>
  </EventDetails>

  </div>

      <FullCalendar class="demo-app-calendar" :options="calendarOptions">
        <template v-slot:eventContent="arg">
          <b>{{ arg.timeText }}</b>
          <i>{{ arg.event.title }}</i>
        </template>
      </FullCalendar>
    </div>
  </div>
</div >


</template>



<style lang='scss'>

h1,p {
   margin-bottom: 16px;
 }

 h1 {
  font-size: 32px;
    }
p {
  font-size: 18px;
  }
button {
  padding: 7px 15px;
  border: none;
  font-size: 16px;
  background-color: crimson;
  color: #fff;
  cursor: pointer;
}

.demo-app-sidebar-section {
  line-height: 1.5;
  background: #eaf9ff;
  border-right: 1px solid #d3e2e8;
  padding: 2em;

  height: 100%; /* Full-height: remove this if you want "auto" height */
  width: 270px; /* Set the width of the sidebar */
  position: fixed; /* Fixed Sidebar (stay in place on scroll) */
  z-index: 1; /* Stay on top */
  top: 0; /* Stay at the top */
  left: 0;
  overflow-x: hidden; /* Disable horizontal scroll */
  padding-top: 20px;
}

h2 {
  margin: 0;
  font-size: 16px;
}
ul {
  margin: 0;
  padding: 0 0 0 1.5em;
}
li {
  margin: 1.5em 0;
  padding: 0;
}
b {
  /* used for event dates/times */
  margin-right: 3px;
}
.demo-app {
  display: flex;
  min-height: 100%;
  font-family: Arial, Helvetica Neue, Helvetica, sans-serif;
  font-size: 14px;
}
.demo-app-main {
  flex-grow: 1;
  padding: 3em;
}
.fc {
  /* the calendar root */
  max-width: 1100px;
  margin-left: 300px; /* Same as the width of the sidebar */
  padding: 0px 10px;
}
</style>
