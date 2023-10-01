document.getElementById("start").addEventListener("click", function ()
{
    chrome.tabs.query({ active: true, currentWindow: true }, function(tabs) 
    {
        chrome.runtime.connect({name: "popup" }).postMessage({
            action: "start",
            duration: 10000 // Set duration as per requirements
        });
    });
});
chrome.runtime.onConnect.addListener(function (port)
{
    if (port.name === "record") {
        port.onMessage.addListener(function (message) {
            if (message.action === "saved") {
                document.getElementById("preview").src = message.url;
            }
        });
    }
});