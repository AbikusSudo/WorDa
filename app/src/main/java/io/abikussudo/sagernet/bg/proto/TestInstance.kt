package io.abikussudo.sagernet.bg.proto

import io.abikussudo.sagernet.BuildConfig
import io.abikussudo.sagernet.bg.GuardedProcessPool
import io.abikussudo.sagernet.database.ProxyEntity
import io.abikussudo.sagernet.fmt.buildConfig
import io.abikussudo.sagernet.ktx.Logs
import io.abikussudo.sagernet.ktx.runOnDefaultDispatcher
import io.abikussudo.sagernet.ktx.tryResume
import io.abikussudo.sagernet.ktx.tryResumeWithException
import kotlinx.coroutines.delay
import libcore.Libcore
import moe.matsuri.nb4a.net.LocalResolverImpl
import kotlin.coroutines.suspendCoroutine

class TestInstance(profile: ProxyEntity, val link: String, private val timeout: Int) :
    BoxInstance(profile) {

    suspend fun doTest(): Int {
        return suspendCoroutine { c ->
            processes = GuardedProcessPool {
                Logs.w(it)
                c.tryResumeWithException(it)
            }
            runOnDefaultDispatcher {
                use {
                    try {
                        init()
                        launch()
                        if (processes.processCount > 0) {
                            // wait for plugin start
                            delay(500)
                        }
                        c.tryResume(Libcore.urlTest(box, link, timeout))
                    } catch (e: Exception) {
                        c.tryResumeWithException(e)
                    }
                }
            }
        }
    }

    override fun buildConfig() {
        config = buildConfig(profile, true)
    }

    override suspend fun loadConfig() {
        // don't call destroyAllJsi here
        if (BuildConfig.DEBUG) Logs.d(config.config)
        box = Libcore.newSingBoxInstance(config.config, LocalResolverImpl)
    }

}
