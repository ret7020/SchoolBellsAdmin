const openBellManager = (url, password) => {
    window.open(`${url}/api/inline_auth?password=${password}`, "_blank");
};
