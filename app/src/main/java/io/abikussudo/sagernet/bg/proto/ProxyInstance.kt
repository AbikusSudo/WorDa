package io.abikussudo.sagernet.bg.proto

import io.abikussudo.sagernet.BuildConfig
import io.abikussudo.sagernet.bg.BaseService
import io.abikussudo.sagernet.bg.ServiceNotification
import io.abikussudo.sagernet.database.ProxyEntity
import io.abikussudo.sagernet.ktx.Logs
import io.abikussudo.sagernet.ktx.runOnDefaultDispatcher
import kotlinx.coroutines.runBlocking
import moe.matsuri.nb4a.utils.JavaUtil

class ProxyInstance(profile: ProxyEntity, var service: BaseService.Interface? = null) :
    BoxInstance(profile) {

    var notTmp = true

    var lastSelectorGroupId = -1L
    var displayProfileName = ServiceNotification.genTitle(profile)

    // for TrafficLooper
    var looper: TrafficLooper? = null

    override fun buildConfig() {
        super.buildConfig()
        lastSelectorGroupId = super.config.selectorGroupId
        //
        if (notTmp) Logs.d(config.config)
        if (notTmp && BuildConfig.DEBUG) Logs.d(JavaUtil.gson.toJson(config.trafficMap))
    }

    // only use this in temporary instance
    fun buildConfigTmp() {
        notTmp = false
        buildConfig()
    }

    override suspend fun init() {
        super.init()
        pluginConfigs.forEach { (_, plugin) ->
            val (_, content) = plugin
            Logs.d(content)
        }
    }

    override suspend fun loadConfig() {
        super.loadConfig()
    }

    override fun launch() {
        box.setAsMain()
        super.launch() // start box
        runOnDefaultDispatcher {
            looper = service?.let { TrafficLooper(it.data, this) }
            looper?.start()
        }
    }

    override fun close() {
        super.close()
        runBlocking {
            looper?.stop()
            looper = null
        }
    }
}
