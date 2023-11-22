import { Suspense, lazy, onCleanup, onMount } from 'solid-js'
import { Route, Routes } from '@solidjs/router'
import Login from './pages/Login'
import Sidebar from './components/Sidebar'
import NotFound from './pages/NotFound'
import Protected from './components/Protected'
import LoadingAnimation from './components/LoadingAnimation'
import Home from './pages/Home'
import History from './pages/History'
import Setting from './pages/Setting'
import { authStore } from "./store/authStore";


function App() {
  let intervalId: number;

  onMount(() => {
    intervalId = setInterval(fetchData, 10000); // 10000 milliseconds = 10 seconds

  });

  const fetchData = async () => {
    if (authStore.sessionId === null) return;
    // try {
    //   const response = await fetch(`http://localhost:8000/update-login-session/${upcomingClass()!.courseCode}`);
    //   const data = await response.json();
    //   console.log(data);
    // } catch (error) {
    //   console.error('Error fetching data:', error);
    // }
  };

  onCleanup(() => {
    clearInterval(intervalId);
  });

  return (
    <>
      <Suspense fallback={<LoadingAnimation/>}>
        <Routes>
          <Route path="/auth/login" component={Login} />
          <Route path="/*" element={<Protected><Sidebar/></Protected>}>
            <Route path="/" component={Home} />
            <Route path="/home" component={Home} />
            <Route path="/history" component={History} />
            <Route path="/setting" component={Setting} />
          </Route>
          <Route path="/*" component={NotFound} />
        </Routes>
      </Suspense>
    </>
  )
}

export default App
