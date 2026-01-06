package io.abikussudo.sagernet.ui.profile

import io.abikussudo.sagernet.fmt.v2ray.VMessBean

class VMessSettingsActivity : StandardV2RaySettingsActivity() {

    override fun createEntity() = VMessBean().apply {
        if (intent?.getBooleanExtra("vless", false) == true) {
            alterId = -1
        }
    }

}