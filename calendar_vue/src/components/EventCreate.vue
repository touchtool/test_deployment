<template>
	<div>
		<CreateEvent style="text-align: center;" v-if="popupTriggers.buttonTrigger" 
		:TogglePopup="() => TogglePopup('buttonTrigger')">
			<div class="popup-background">
				<div class="popup">
					<h1 style="font-size: 50px;">New Event</h1>
					<form @submit.prevent="eventCreate" class="event-create-form">
						<textarea type="name" required v-model="name"
							placeholder="Title"
							maxlength="60" rows="1" cols="50"></textarea>
						<p></p>
						<textarea type="description" v-model="description" 
							placeholder="Description (optional)"
							maxlength="600" rows="5" cols="50"></textarea>
						<table class="table-input">
							<tr>
								<td>Start</td>
								<td>Date  <input class="event-input" type="date" required v-model="start_date"></td>
							</tr>
							<tr>
								<td></td>
								<td>Time  <input class="event-input" type="time" required v-model="start_time"></td>
							</tr>
							<tr>
								<td>End</td>
								<td>Date  <input class="event-input" type="date" required v-model="end_date"></td>
							</tr>
							<tr>
								<td></td>
								<td>Time  <input class="event-input" type="time" required v-model="end_time"></td>
							</tr>
						</table>
						<div class="footer">
							<button class="app-button" type="submit">Done</button>
							<button class="app-button-cancel" @click="() => TogglePopup('buttonTrigger')">Cancel</button>
						</div>
					</form>
				</div>
			</div>
		</CreateEvent>
		<button class="app-button-tp" style="font-size: 40px;" @click="() => TogglePopup('buttonTrigger')">+</button>
	</div>
</template>

<script>
import { ref } from 'vue';
import axios from 'axios';

export default {
	setup () {
		const popupTriggers = ref({
			buttonTrigger: false,
		});

		const TogglePopup = (trigger) => {
			popupTriggers.value[trigger] = !popupTriggers.value[trigger]
		}
		return {
			popupTriggers,
			TogglePopup
		}
	},
	data() {
		return {
			name: '',
			description: '',
			start_date: '',
			start_time: '',
			end_date: '',
			end_time: ''
		}
	},
	methods: {
		eventCreate() {
			const start_date_time = this.start_date + " " + this.start_time + ":00"
			const end_date_time = this.end_date + " " + this.end_time + ":00"
			const event = {
				"name" : this.name,
				"description" : this.description,
				"start_date" : start_date_time,
				"end_date" : end_date_time
			}
			const calendar_slug = this.$route.params.calendar_slug

			// console.log(this.name)
			// console.log(this.description)
			// console.log(start_date_time)
			// console.log(end_date_time)

			axios.post(`/api/calendar/${calendar_slug}/`, event)
				.then(function(response) {
					console.log(response),
					window.location.reload()
					})
				.catch(function(error) {
					console.log(error),
					alert("Opps, " + error)
					})
		}
	},
}

</script>

<style>
@import './../assets/style.css';
@import './../assets/color.css';

.event-create-form {
	color: var(--black);
	text-align: left;
	font-size: 20px;
	margin: 20x;
	padding: 10px;
}

textarea {
	background: var(--gray-light);
	font-size: 20px;
	display: block;
	padding: 10px 20px;
	border: none;
	border-radius: 8px;
	resize: vertical;
}

.event-input {
	background: var(--gray-light);
	font-size: 20px;
	padding: 10px;
	width: 200px;
	border: none;
	border-radius: 8px;
}

.table-input {
	width: 104%;
	text-align: end;
	border-spacing: 20px;
}

.popup-background {
	background-color: var(--black-op);
	position: fixed;
	top: 0;
	left: 0;
	right: 0;
	bottom: 0;
	z-index: 1;
	display: flex;
	align-items: center;
	justify-content: center;
	padding: 50px;

	animation-name: fade;
	animation-duration: 0.5s

}
.popup {
	background: var(--white);
	color: var(--black);
	height: 100%;
	overflow: auto;
	padding: 20px;
}

.footer {
	display: flex;
	justify-content: space-evenly; 
}

</style>