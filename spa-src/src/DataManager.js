// SPDX-FileCopyRightText: Copyright (c) 2023-present Jeffrey LeBlanc
// SPDX-License-Indentifier: MIT

import {reactive} from "vue"

export default class DataManager {

    constructor(){
        this.store = reactive({
            posts: []
        });
    }

    async fetch_posts(){
        const get_resp = await window.fetch("/api/v1/posts/");
        const resp_obj = await get_resp.json();
        for(let post of resp_obj){
            console.log("push:",post)
            this.store.posts.push(post)
        }
    }

    async push_post({title="",content=""}={}){
        const post_resp = await window.fetch("/api/v1/posts/",{
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({title,content})
        });
        const resp_obj = await post_resp.json();
        console.log("resp_obj:",resp_obj);
        this.store.posts.push(resp_obj)
    }
}
