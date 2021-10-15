<template>
	<div>
		<CreateEvent style="text-align: center;" v-if="popupTriggers.buttonTrigger" 
		:TogglePopup="() => TogglePopup('buttonTrigger')">
			<div class="event-create">
				<div class="create">
					<h1 style="font-size: 50px; color: black;">New Event</h1>
					<form>
						<textarea type="name" required v-model="name"
							placeholder="Title"
							maxlength="60" rows="1" cols="50"></textarea>
						<p></p>
						<textarea type="description" v-model="description" 
							placeholder="Description (optional)"
							maxlength="600" rows="5" cols="50"></textarea>
						<table style="width: 100%; text-align: end;">
							<tr>
								<td>Start</td>
								<td>Date<input type="date" required v-model="start_date"></td>
							</tr>
							<tr>
								<td></td>
								<td>Time<input type="time" required step="2" v-model="start_time"></td>
							</tr>
							<tr>
								<td>End</td>
								<td>Date<input type="date" required v-model="end_date"></td>
							</tr>
							<tr>
								<td></td>
								<td>Time<input type="time" required step="2" v-model="end_time"></td>
							</tr>
						</table>
						<div class="submit">
							<button @click="() => eventCreate()">Done</button>
							<button style="background: gray;" @click="() => TogglePopup('buttonTrigger')">Cancel</button>
						</div>
					</form>
				</div>
			</div>
		</CreateEvent>
		<button style="font-size: 40px; margin-top: 5px;" @click="() => TogglePopup('buttonTrigger')">+</button>
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
			const start_date_time = this.start_date + " " + this.start_time
			const end_date_time = this.end_date + " " + this.end_time
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
					TogglePopup('buttonTrigger'),
					window.location.reload()
					})
				.catch(function(error) {console.log(error)})
		}
	},
}

</script>

<style>
	form {
		margin: 20x;
		padding: 10px;
		font-size: 20px;
		color: rgb(0, 0, 0, 0.5);
		text-align: left;
	}

	textarea {
		display: block;
		padding: 10px 20px;
		border: none;
		background: whitesmoke;
		border-radius: 8px;
		font-size: 20px;
		resize: vertical;
	}

	input {
		padding: 5px 10px;
		width: 200px;

		border: none;
		/* border-bottom: 1px solid #ddd; */
		background: whitesmoke;
		font-size: 20px;
		/* display: block; */
		border-radius: 8px;
	}

	button {
		background: rgb(0, 102, 100);
		border: 0;
		padding: 10px 20px;
		margin-top: 20px;
		color: white;
		font-size: 20px;
		cursor: pointer;
		border-radius: 8px;
	}

	.event-create {
		position: fixed;
		top: 0;
		left: 0;
		right: 0;
		bottom: 0;
		z-index: 0;
		background-color: rgba(0, 0, 0,0.3);
		
		display: flex;
		align-items: center;
		justify-content: center;
	}

	.create {
	background: #FFF;
	padding: 20px;
	}

	.submit {
		display: flex;
		justify-content: space-evenly; 
	}

</style>