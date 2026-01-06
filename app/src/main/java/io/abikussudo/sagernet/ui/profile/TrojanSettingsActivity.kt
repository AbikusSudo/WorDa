package io.abikussudo.sagernet.ui.profile

import io.abikussudo.sagernet.fmt.trojan.TrojanBean

class TrojanSettingsActivity : StandardV2RaySettingsActivity() {

    override fun createEntity() = TrojanBean()

}
