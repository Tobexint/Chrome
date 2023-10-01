chrome.runtime.onConnect.addListener(function (port) 
{
    if (port.name === "record") 
    {
        port.onMessage.addListener (function (message)     
        {
            if (message.action === "start") 
            {
                chrome.tabCapture.capture({ video: true, audio: true }, function(stream)
                {
                    let mediaRecorder = new MediaRecorder(stream);
                    let chunks = [];

                    mediaRecorder.ondataavailable = function (e) {
                        chunks.push(e.data);
                    };
                    mediaRecorder.onstop = function () {
                        let blob = new Blob (chunks, { type: "video/webm" });
                        let url = URL.createObjectURL(blob);
                        const formData = new FormData();
                        formData.append("video", blob, "recording.webm");

                        fetch("http://localhost:5000/upload", {
                            method: "POST",
                            body: formData,
                        })
                        .then((data) => {
                            port.postMessage({ action: "started" });
                            setTimeout(function () {
                                mediaRecorder.stop();
                            }, message.duration); 
                        });
                    }
                });
            }
        });
    }
})