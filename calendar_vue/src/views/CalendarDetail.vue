<template>
    <div class="calendar-events">
        <h1>List of events</h1>
        <!-- <div v-for="e in calendar_events" v-bind:key="e.id">
            <h2>{{ e.name }}</h2>
            <p>{{ e.description }}</p>
            <p>{{ e.start_date }}</p>
            <p>{{ e.end_date }}</p>
            <router-link v-bind:to="e.get_absolute_url">View detail</router-link>
        </div> -->
        <Calendar v-bind:calendar_data="calendar_events" />
    </div>
</template>

<script>
import Calendar from "../components/Calendar"
import axios from 'axios'

export default {
  name: 'Home',
  components: {
    Calendar
  },
  data() {
      return {
          calendar_events: []
      }
  },
  mounted() {
      this.getCalendarEvents()
  },
  methods: {
      getCalendarEvents() {
          const calendar_slug = this.$route.params.calendar_slug
          console.log(calendar_slug)

          axios
            .get(`/api/calendar/${calendar_slug}`)
            .then(response => {
                this.calendar_events = response.data
            })
            .catch(error => {
                console.log(error)
            })
      }
  }
}
</script>
