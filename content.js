chrome.runtime.onConnect.addListener(function (port)
{
    if (port.name === "popup"){
        port.onMessage.addListener(function(message){
            if (message.action === "start") {
                chrome.runtime.connect({name: "record"}).postMessage({
                    action: "start",
                    duration: message.duration,
                });
            }
        });
    }
});