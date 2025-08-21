function getEVId() {
    let storedEVId = localStorage.getItem("evID");
    if (!storedEVId) {
        storedEVId = crypto.randomUUID();
        localStorage.setItem("evID", storedEVId);
    }
    return storedEVId;
}