<template>
    <div class="fileUploadContainer" @dragenter.prevent="setActive" @dragover.prevent="setActive" @dragleave.prevent="setInactive" @drop.prevent="onDrop">
        <template v-if="!active">
            <h4 class="fileUploadTitle">Přetáhněte své soubory</h4>
            <p class="fileUploadText">Nebo</p>
            <label class="fileUploadButton">
             Klikněte sem
                <input type="file" name="fileUpload" multiple="multiple" style="display: none;" @input="onManualUpload"/>
            </label>
        </template>
        <h4 v-else class="fileUploadTitle">Pusťe soubory</h4>
        <div v-if="files.length != 0" class="fileUploadFilePreviewContainer">
            <TransitionGroup name="fadeSlide">
                <template v-for="(file, index) in files" :key="file.name">
                    <div class="filePreview" @click="removeFile(index)">
                        <img class="filePreviewImage" :src="file.url" />
                        <img class="filePreviewDeleteIcon" :src="require('@/assets/icons/delete.svg')"/>
                    </div>
                </template>
            </TransitionGroup>
        </div>
        <ButtonAction @click="uploadFiles" v-if="files.length != 0">Nahrát vybrané soubory</ButtonAction>
    </div>    
</template>

<script>
import ButtonAction from './ButtonAction.vue';
export default {
  name: 'FileUpload',
  components: {
    ButtonAction
},
  props: {
  },

  methods: {
    setActive: function() {
        clearTimeout(this.activeTimeout);
        this.active = true;
    },
    setInactive: function() {
        this.activeTimeout = setTimeout(() => {
            this.active = false;
        }, 50)
    },

    filterNewFiles: function(uploadedFiles){
        let newFiles = []
        let dupe = false;

        for (let i = 0; i < uploadedFiles.length; i++){
            dupe = false;
            for (let o = 0; o < this.files.length; o++){
                if (uploadedFiles[i].name === this.files[o].name){
                    dupe = true;
                    break;
                }
            }
            if (!dupe){
                newFiles.push(uploadedFiles[i]);
            }
        }

        console.log(newFiles)
        console.log(uploadedFiles)

        for (let i = 0; i < newFiles.length; i++) {
            newFiles[i].url = URL.createObjectURL(newFiles[i]);
        }   

        console.log(newFiles)
        this.files = [...this.files, ...newFiles];
    },
    onDrop: function(e) {
        this.active = false;
        this.filterNewFiles(e.dataTransfer.files);
    },
    removeFile: function(index) {
        if (this.files.length == 1){
            this.files = []
        }
        else {
            this.files.splice(index, 1);
            console.log(this.files);
        }
    },
    onManualUpload: function(e){
       this.filterNewFiles(e.target.files);
       console.log(e)
    },
    uploadFiles: async function(){
        let convertedFiles = []

        for (let file of this.files){
            convertedFiles.push(new File([await fetch(file.url).then(r => r.blob())], file.name,
            {
                type: file.type, 
                lastModified: new Date().getTime()
            }))
        }
        this.$emit("uploadFiles", convertedFiles)
    }
  },

  data: function () {
      return {
          active: false,    
          activeTimeout: null,
          files: []
      }
  }
}
</script>

<style scoped lang="scss">

@import url('https://fonts.googleapis.com/css2?family=Montserrat:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;1,100;1,200;1,300;1,400;1,500;1,600;1,700&display=swap');
@import "@/assets/colors.scss";

.fileUploadContainer {
    width: 100%;
    box-sizing: border-box;
    padding: 5%;
    border: #F1F1F1 dashed 5px;
    border-radius: 2px;
    display: flex;
    flex-flow: column nowrap;
    align-items: center;
    justify-content: center;
    min-height: 250px;
    z-index: 2;
    transition: all 220ms ease-in-out;

    .fileUploadFilePreviewContainer {
        display: flex;
        flex-flow: row nowrap;
        width: 80%;
        overflow-x:auto;
        overflow-y: hidden;
        align-items: center;
        justify-content: center;
        margin: 20px 0 20px 0;
    }

    .fileUploadTitle {
        font-size: 1.5rem;
        font-weight: 600;
        margin: 0 0 10px 0;
        z-index: 1;
    }

    .fileUploadText {
        font-size: 1rem;
        font-weight: 400;
        margin: 0 0 10px 0;
        z-index: 1;
    }

    .fileUploadButton {
        background-position: center;
        transition: background 400ms;
        border: none;
        padding: 8px 14px;
        background-color: $primary;
        box-shadow: 0px 3px 3px rgba(0, 0, 0, 0.25);
        cursor: pointer;
        text-decoration: none;
        font-size: 0.875;
        font-weight: 700;
        color: $background-light;
        font-family: 'Montserrat', sans-serif;
        z-index: 1;


        &:hover {
        background: $primary radial-gradient(circle, transparent 1%, $primary 1%) center/15000%;
        }

        &:active {
        background-color: $secondary;
        background-size: 100%;
        transition: background 0ms;
        }
    }
}

.filePreview {
    height: 124px;
    width: 100px;
    display: flex;
    flex-flow: column nowrap;
    align-items: center;
    justify-content: center;
    margin: -24px 5px 5px 5px;
    cursor: pointer;
    animation: AppearAnimation 220ms ease-in-out;

    &:hover {
        .filePreviewImage {
            filter: brightness(0.45);
        }

        .filePreviewDeleteIcon {
            opacity: 1;
        }
    }

    .filePreviewImage {
        height: 100px;
        width: 100px;
        margin: 0 0 0 0;
        object-fit: cover;
        filter: brightness(0.75);
        z-index: 1;
        transition: all 220ms ease-in-out;
    }

    .filePreviewDeleteIcon {
        margin: -62px 0 0 0;
        z-index: 2;
        opacity: 0;
        transition: all 220ms ease-in-out;
    }
}

.fadeSlide-enter-active {
    transition: all 220ms ease-in-out;
}

.fadeSlide-leave-active {
    transition: all 220ms ease-in-out;
}

.fadeSlide-enter-from {
    transform: translateX(20px);
    opacity: 0;
}

.fadeSlide-move {
    transition: all 220ms ease-in-out;
}

.fadeSlide-leave-to {
    transform: translateX(20px);
    opacity: 0;
}

.fadeSlide-enter-to {
    transform: translateX(0px);
    opacity: 1;
}

.fadeSlide-leave-from {
    transform: translateX(0px);
    opacity: 1;
}

@keyframes AppearAnimation {
    from {
        opacity: 0;
        transform: translateX(20px);
    }
    to {
        opacity: 1;
        transform: translateX(0px);
    }
}

</style>
