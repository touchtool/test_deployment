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
        select: this.handleDateSelect,
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
    // console.log("mounted calendar events", this.calendar_events)
    // console.log("mounted events", this.calendarOptions.events)
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
      //delete
      // if (confirm(`Are you sure you want to delete the event '${clickInfo.event.title}'`)) {
      //   clickInfo.event.remove()
      // }
      //debug
      // let calendarApi = clickInfo.view.calendar;
      // console.log(clickInfo.event);

      this.event_details = [clickInfo.event.title, clickInfo.event.start, clickInfo.event.end]
      this.modalActive = true;
      console.log(this.modalActive)
    },
    handleEvents(events) {
      this.currentEvents = events;
    },
  },
};
</script>
<template>

  <!--Details-->
  <EventDetails v-show:modalActive="modalActive">
      <div class="modal-content">
        <h1>{{ event_details[0] }}</h1>
        <p>start date: {{ event_details[1] }}</p>
          <p>end date:{{ event_details[2] }}</p>
      </div>
  </EventDetails>



  <div class="demo-app">
    <div class="demo-app-main">
      <FullCalendar class="demo-app-calendar" :options="calendarOptions">
        <template v-slot:eventContent="arg">
          <b>{{ arg.timeText }}</b>
          <i>{{ arg.event.title }}</i>
        </template>
      </FullCalendar>
    </div>
  </div>




</template>



<style lang='css'>
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
  margin: 0 auto;
}
</style>
