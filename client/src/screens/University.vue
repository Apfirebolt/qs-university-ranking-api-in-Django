<template>
  <div class="min-h-screen bg-info flex items-center justify-center">
    <div class="bg-white shadow-lg rounded-lg p-4">
      <h1 class="text-4xl font-bold text-primary text-center mb-4">Universities</h1>
      <p class="text-gray-700 leading-relaxed mb-4">
        Explore the mysteries of their existence, learn about their habitats,
        and uncover the secrets of their extinction. Whether you're a
        paleontology enthusiast or just curious, there's always something new to
        discover about universities.
      </p>

      <Loader v-if="loading" />

      <div v-if="universityData && universityData.results" class="grid gap-4 mb-4">
        <div
          v-for="university in universityData.results"
          :key="university.id"
          class="bg-gray-50 border border-gray-200 rounded-lg p-4 shadow-sm"
        >
          <div class="flex justify-between items-start mb-3">
            <h2 class="text-xl font-semibold text-gray-800">{{ university.name }}</h2>
            <span class="bg-primary text-white px-2 py-1 rounded text-sm font-medium">
              Rank #{{ university.rank }}
            </span>
          </div>
          
          <div class="grid grid-cols-2 gap-2 text-sm text-gray-600 mb-3">
            <p><span class="font-medium">Country:</span> {{ university.country }}</p>
            <p><span class="font-medium">Location:</span> {{ university.location }}</p>
            <p><span class="font-medium">Score:</span> {{ university.score_scaled }}</p>
          </div>
          
          <div class="grid grid-cols-3 gap-2 text-xs text-gray-500">
            <div class="text-center p-2 bg-white rounded">
              <p class="font-medium">AR</p>
              <p>{{ university.ar_rank }} ({{ university.ar_score }})</p>
            </div>
            <div class="text-center p-2 bg-white rounded">
              <p class="font-medium">FSR</p>
              <p>{{ university.fsr_rank }} ({{ university.fsr_score }})</p>
            </div>
            <div class="text-center p-2 bg-white rounded">
              <p class="font-medium">IRN</p>
              <p>{{ university.irn_rank }} ({{ university.irn_score }})</p>
            </div>
          </div>
        </div>
      </div>

      <div class="flex justify-between mt-4">
        <button
          @click="goToPreviousPage"
          :disabled="!universityData || !universityData.previous"
          class="bg-primary text-white px-4 py-2 rounded hover:bg-blue-600"
        >
          Previous
        </button>
        <button
          @click="goToNextPage"
          :disabled="!universityData || !universityData.next"
          class="bg-primary text-white px-4 py-2 rounded hover:bg-blue-600"
        >
          Next
        </button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { onMounted, ref } from "vue";
import axios from "axios";
import Loader from "../components/Loader.vue";

const universityData = ref(null);
const loading = ref(false);
const currentPage = ref(1);


const getUniversityData = async () => {
  try {
    loading.value = true;
    const response = await axios.get(
      `http://localhost:8000/api/university?page=${currentPage.value}`
    );
    universityData.value = response.data;
  } catch (error) {
    console.error("Error fetching university data:", error);
  } finally {
    loading.value = false;
  }
};

const goToNextPage = () => {
  if (universityData.value && universityData.value.next) {
    currentPage.value++;
    getUniversityData();
  }
};

const goToPreviousPage = () => {
  if (universityData.value && universityData.value.previous) {
    currentPage.value--;
    getUniversityData();
  }
};

onMounted(() => {
  getUniversityData();
});
</script>
