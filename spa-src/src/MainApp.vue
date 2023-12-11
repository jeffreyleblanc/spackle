<!--
SPDX-FileCopyRightText: Copyright (c) 2023-present Jeffrey LeBlanc
SPDX-License-Indentifier: MIT
-->

<template>
<main class="flex flex-col gap-y-8 p-4 font-sans">
    <nav class="flex flex-row items-center">
        <!-- we need to :src trick so rollup doesn't complain -->
        <img class="h-24" :src="'/files/example.svg'"/>
        <h1 class="text-2xl font-bold">Welcome to Spackle</h1>
    </nav>
    <section class="flex flex-col gap-y-2">
        <h1 class="text-xl font-bold">
            Add a Post:
        </h1>
        <label class="text-sm text-gray-600">
            Title
        </label>
        <input class="max-w-2xl px-4 py-2 border border-gray-600 rounded"
               type="text" v-model="local_title"
        />
        <label class="text-sm text-gray-600">
            Content
        </label>
        <input class="max-w-2xl px-4 py-2 border border-gray-600 rounded"
               type="text" v-model="local_content"
        />
        <button @click="submit_post" class="w-fit px-4 py-2 bg-blue-600 text-white rounded hover:bg-blue-700">
            Add Post
        </button>
    </section>
    <section class="flex flex-col gap-y-4">
        <h1 class="text-xl font-bold">Posts:</h1>
        <div class="p-4 bg-gray-200 rounded"
            v-for="post in posts"
            :key="post.id"
        >
            <div class="font-bold">{{post.title}}</div>
            <div>{{post.content}}</div>
        </div>
    </section>
</main>
</template>

<script>

export default {
    data(){ return {
        local_title: "",
        local_content: ""
    } },
    computed: {
        posts(){ return this.$G.mng.store.posts.sort((a,b) => b.id-a.id) }
    },
    methods: {
        submit_post(){
            const title = this.local_title.trim();
            const content = this.local_content.trim();
            if(title=="" || content==""){
                alert("Empty title or content!");
                return;
            }

            console.log({title,content});
            this.local_title = "";
            this.local_content = "";
            this.$G.mng.push_post({title,content});
        }
    }
}
</script>

