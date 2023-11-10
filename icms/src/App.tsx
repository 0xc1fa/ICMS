import { Suspense, lazy } from 'solid-js'
import { Route, Routes } from '@solidjs/router'
import Login from './pages/Login'
import Sidebar from './components/Sidebar'
import NotFound from './pages/NotFound'
import Protected from './components/Protected'
import LoadingAnimation from './components/LoadingAnimation'
import Home from './pages/Home'
import History from './pages/History'
import Setting from './pages/Setting'


function App() {

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
