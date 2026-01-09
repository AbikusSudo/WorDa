import os
import re
import json
import socket
import random
import asyncio
import logging
import base64
import requests
import httpx
import urllib3
from urllib.parse import quote, urlsplit, urlunsplit, unquote
from datetime import datetime
from functools import lru_cache
from collections import defaultdict

URLS = [
    "https://raw.githubusercontent.com/MrAbolfazlNorouzi/iran-configs/refs/heads/main/configs/working-configs.txt",
    "https://raw.githubusercontent.com/arshiacomplus/v2rayExtractor/refs/heads/main/mix/sub.html",
    "https://www.v2nodes.com/subscriptions/country/all/?key=CCAD69583DBA2BF",
    "https://raw.githubusercontent.com/4n0nymou3/multi-proxy-config-fetcher/refs/heads/main/configs/proxy_configs.txt",
    "https://fsub.flux.2bd.net/bypass/bypass-all.txt",
    "https://raw.githubusercontent.com/igareck/vpn-configs-for-russia/refs/heads/main/Vless-Reality-White-Lists-Rus-Cable.txt",
    "https://raw.githubusercontent.com/igareck/vpn-configs-for-russia/refs/heads/main/Vless-Reality-White-Lists-Rus-Mobile.txt",
    "https://raw.githubusercontent.com/zieng2/wl/main/vless.txt",
    "https://raw.githubusercontent.com/zieng2/wl/refs/heads/main/vless_universal.txt",
    "https://raw.githubusercontent.com/zieng2/wl/main/vless_lite.txt",
    "https://jsnegsukavsos.hb.ru-msk.vkcloud-storage.ru/love",
    "https://raw.githubusercontent.com/LowiKLive/BypassWhitelistRu/refs/heads/main/WhiteList-Bypass_Ru.txt",
    "https://raw.githubusercontent.com/55prosek-lgtm/vpn_config_for_russia/refs/heads/main/whitelist.txt",
    "https://github.com/sakha1370/OpenRay/raw/refs/heads/main/output/all_valid_proxies.txt",
    "https://raw.githubusercontent.com/sevcator/5ubscrpt10n/main/protocols/vl.txt",
    "https://raw.githubusercontent.com/yitong2333/proxy-minging/refs/heads/main/v2ray.txt",
    "https://raw.githubusercontent.com/acymz/AutoVPN/refs/heads/main/data/V2.txt",
    "https://raw.githubusercontent.com/miladtahanian/V2RayCFGDumper/refs/heads/main/config.txt",
    "https://raw.githubusercontent.com/roosterkid/openproxylist/main/V2RAY_RAW.txt",
    "https://github.com/Epodonios/v2ray-configs/raw/main/Splitted-By-Protocol/trojan.txt",
    "https://raw.githubusercontent.com/YasserDivaR/pr0xy/refs/heads/main/ShadowSocks2021.txt",
    "https://raw.githubusercontent.com/mohamadfg-dev/telegram-v2ray-configs-collector/refs/heads/main/category/vless.txt",
    "https://raw.githubusercontent.com/mheidari98/.proxy/refs/heads/main/vless",
    "https://raw.githubusercontent.com/youfoundamin/V2rayCollector/main/mixed_iran.txt",
    "https://raw.githubusercontent.com/mheidari98/.proxy/refs/heads/main/all",
    "https://github.com/Kwinshadow/TelegramV2rayCollector/raw/refs/heads/main/sublinks/mix.txt",
    "https://github.com/LalatinaHub/Mineral/raw/refs/heads/master/result/nodes",
    "https://raw.githubusercontent.com/miladtahanian/multi-proxy-config-fetcher/refs/heads/main/configs/proxy_configs.txt",
    "https://github.com/MhdiTaheri/V2rayCollector_Py/raw/refs/heads/main/sub/Mix/mix.txt",
    "https://github.com/Epodonios/v2ray-configs/raw/main/Splitted-By-Protocol/vmess.txt",
    "https://github.com/MhdiTaheri/V2rayCollector/raw/refs/heads/main/sub/mix",
    "https://github.com/Argh94/Proxy-List/raw/refs/heads/main/All_Config.txt",
    "https://raw.githubusercontent.com/shabane/kamaji/master/hub/merged.txt",
    "https://raw.githubusercontent.com/wuqb2i4f/xray-config-toolkit/main/output/base64/mix-uri",
    "https://raw.githubusercontent.com/AzadNetCH/Clash/refs/heads/main/AzadNet.txt",
    "https://raw.githubusercontent.com/STR97/STRUGOV/refs/heads/main/STR.BYPASS#STR.BYPASS%F0%9F%91%BE",
    "https://raw.githubusercontent.com/V2RayRoot/V2RayConfig/refs/heads/main/Config/vless.txt",
    "https://raw.githubusercontent.com/4n0nymou3/multi-proxy-config-fetcher/refs/heads/main/configs/proxy_configs.txt",
    "https://raw.githubusercontent.com/MatinGhanbari/v2ray-configs/main/subscriptions/v2ray/all_sub.txt",
    "https://raw.githubusercontent.com/barry-far/V2ray-Config/refs/heads/main/All_Configs_Sub.txt",
    "https://raw.githubusercontent.com/ebrasha/free-v2ray-public-list/refs/heads/main/all_extracted_configs.txt",
    "https://raw.githubusercontent.com/SoliSpirit/v2ray-configs/refs/heads/main/all_configs.txt",
    "https://raw.githubusercontent.com/mahdibland/V2RayAggregator/refs/heads/master/sub/sub_merge.txt",
    "https://raw.githubusercontent.com/F0rc3Run/F0rc3Run/refs/heads/main/Best-Results/proxies.txt",
    "https://raw.githubusercontent.com/Surfboardv2ray/TGParse/refs/heads/main/configtg.txt",
    "https://raw.githubusercontent.com/Argh94/V2RayAutoConfig/refs/heads/main/configs/Vless.txt",
    "https://raw.githubusercontent.com/Argh94/V2RayAutoConfig/refs/heads/main/configs/Hysteria2.txt",
    "https://raw.githubusercontent.com/Argh94/V2RayAutoConfig/refs/heads/main/configs/ShadowSocks.txt",
    "https://raw.githubusercontent.com/Argh94/V2RayAutoConfig/refs/heads/main/configs/Trojan.txt",
    "https://raw.githubusercontent.com/Argh94/V2RayAutoConfig/refs/heads/main/configs/Vmess.txt",
    "https://raw.githubusercontent.com/kort0881/vpn-key-vless/refs/heads/main/subscriptions/all.txt",
    "https://raw.githubusercontent.com/NiREvil/vless/main/sub/SSTime",
    "https://raw.githubusercontent.com/ndsphonemy/proxy-sub/refs/heads/main/all.txt",
    "https://raw.githubusercontent.com/Mahdi0024/ProxyCollector/master/sub/proxies.txt",
    "https://raw.githubusercontent.com/Mosifree/-FREE2CONFIG/refs/heads/main/Reality",
    "https://raw.githubusercontent.com/MrMohebi/xray-proxy-grabber-telegram/master/collected-proxies/row-url/all.txt",
    "https://raw.githubusercontent.com/Barabama/FreeNodes/refs/heads/main/nodes/blues.txt",
    "https://raw.githubusercontent.com/Barabama/FreeNodes/refs/heads/main/nodes/clashmeta.txt",
    "https://raw.githubusercontent.com/Barabama/FreeNodes/refs/heads/main/nodes/ndnode.txt",
    "https://raw.githubusercontent.com/Barabama/FreeNodes/refs/heads/main/nodes/nodefree.txt",
    "https://raw.githubusercontent.com/Barabama/FreeNodes/refs/heads/main/nodes/nodev2ray.txt",
    "https://raw.githubusercontent.com/Barabama/FreeNodes/refs/heads/main/nodes/v2rayshare.txt",
    "https://raw.githubusercontent.com/Barabama/FreeNodes/refs/heads/main/nodes/wenode.txt",
    "https://raw.githubusercontent.com/Barabama/FreeNodes/refs/heads/main/nodes/yudou66.txt",
    "https://raw.githubusercontent.com/Firmfox/Proxify/refs/heads/main/v2ray_configs/seperated_by_protocol/vless.txt",
    "https://raw.githubusercontent.com/Firmfox/Proxify/refs/heads/main/v2ray_configs/seperated_by_protocol/vmess.txt",
    "https://raw.githubusercontent.com/Firmfox/Proxify/refs/heads/main/v2ray_configs/seperated_by_protocol/trojan.txt",
    "https://raw.githubusercontent.com/Firmfox/Proxify/refs/heads/main/v2ray_configs/seperated_by_protocol/shadowsocks.txt",
    "https://raw.githubusercontent.com/Firmfox/Proxify/refs/heads/main/v2ray_configs/seperated_by_protocol/other.txt",
    "https://raw.githubusercontent.com/Epodonios/v2ray-configs/refs/heads/main/All_Configs_Sub.txt",
    "https://raw.githubusercontent.com/ALIILAPRO/v2rayNG-Config/refs/heads/main/server.txt",
    "https://github.com/mrvcoder/V2rayCollector/raw/refs/heads/main/vless_iran.txt",
    "https://raw.githubusercontent.com/ssrsub/ssr/refs/heads/master/vless.txt",
    "https://github.com/vxiaov/free_proxies/raw/refs/heads/main/links.txt",
    "https://github.com/peasoft/NoMoreWalls/raw/refs/heads/master/list_raw.txt",
    "https://raw.githubusercontent.com/xiaoji235/airport-free/refs/heads/main/v2ray/clashnodecc.txt",
    "https://raw.githubusercontent.com/xiaoji235/airport-free/refs/heads/main/v2ray/naidounode.txt",
    "https://raw.githubusercontent.com/xiaoji235/airport-free/refs/heads/main/v2ray/v2rayshare.txt",
    "https://github.com/mfuu/v2ray/raw/refs/heads/master/merge/merge.txt",
    "https://raw.githubusercontent.com/chengaopan/AutoMergePublicNodes/refs/heads/master/list_raw.txt",
    "https://raw.githubusercontent.com/mehran1404/Sub_Link/refs/heads/main/V2RAY-Sub.txt",
    "https://raw.githubusercontent.com/V2RAYCONFIGSPOOL/V2RAY_SUB/refs/heads/main/v2ray_configs_no1.txt",
    "https://raw.githubusercontent.com/V2RAYCONFIGSPOOL/V2RAY_SUB/refs/heads/main/v2ray_configs_no2.txt",
    "https://raw.githubusercontent.com/V2RAYCONFIGSPOOL/V2RAY_SUB/refs/heads/main/v2ray_configs_no3.txt",
    "https://raw.githubusercontent.com/V2RAYCONFIGSPOOL/V2RAY_SUB/refs/heads/main/v2ray_configs_no4.txt",
    "https://raw.githubusercontent.com/V2RAYCONFIGSPOOL/V2RAY_SUB/refs/heads/main/v2ray_configs_no5.txt",
    "https://raw.githubusercontent.com/V2RAYCONFIGSPOOL/V2RAY_SUB/refs/heads/main/v2ray_configs_no6.txt",
    "https://raw.githubusercontent.com/V2RAYCONFIGSPOOL/V2RAY_SUB/refs/heads/main/v2ray_configs_no7.txt",
    "https://raw.githubusercontent.com/V2RAYCONFIGSPOOL/V2RAY_SUB/refs/heads/main/v2ray_configs_no8.txt",
    "https://raw.githubusercontent.com/V2RAYCONFIGSPOOL/V2RAY_SUB/refs/heads/main/v2ray_configs_no9.txt",
    "https://raw.githubusercontent.com/V2RAYCONFIGSPOOL/V2RAY_SUB/refs/heads/main/v2ray_configs_no10.txt",
    "https://github.com/nyeinkokoaung404/V2ray-Configs/raw/refs/heads/main/All_Configs_Sub.txt",
    "https://raw.githubusercontent.com/lagzian/SS-Collector/refs/heads/main/mix.txt",
    "https://raw.githubusercontent.com/hamedcode/port-based-v2ray-configs/main/sub/vless.txt",
    "https://raw.githubusercontent.com/hamedcode/port-based-v2ray-configs/main/sub/vmess.txt",
    "https://raw.githubusercontent.com/hamedcode/port-based-v2ray-configs/main/sub/trojan.txt",
    "https://raw.githubusercontent.com/hamedcode/port-based-v2ray-configs/main/sub/ss.txt",
    "https://raw.githubusercontent.com/ninjastrikers/v2ray-configs/main/splitted/vmess.txt",
    "https://raw.githubusercontent.com/ninjastrikers/v2ray-configs/main/splitted/vless.txt",
    "https://raw.githubusercontent.com/ninjastrikers/v2ray-configs/main/splitted/trojan.txt",
    "https://raw.githubusercontent.com/ninjastrikers/v2ray-configs/main/splitted/ss.txt",
    "https://raw.githubusercontent.com/ninjastrikers/v2ray-configs/main/splitted/hysteria.txt",
    "https://raw.githubusercontent.com/R3ZARAHIMI/tg-v2ray-configs-every2h/refs/heads/main/Config_jo.txt",
    "https://raw.githubusercontent.com/itsyebekhe/LiveProxy/refs/heads/main/subscriptions/by_type/plaintext/hy2.txt",
    "https://raw.githubusercontent.com/itsyebekhe/LiveProxy/refs/heads/main/subscriptions/by_type/plaintext/ss.txt",
    "https://raw.githubusercontent.com/itsyebekhe/LiveProxy/refs/heads/main/subscriptions/by_type/plaintext/trojan.txt",
    "https://raw.githubusercontent.com/itsyebekhe/LiveProxy/refs/heads/main/subscriptions/by_type/plaintext/tuic.txt",
    "https://raw.githubusercontent.com/itsyebekhe/LiveProxy/refs/heads/main/subscriptions/by_type/plaintext/vless.txt",
    "https://raw.githubusercontent.com/itsyebekhe/LiveProxy/refs/heads/main/subscriptions/by_type/plaintext/vmess.txt",
    "https://raw.githubusercontent.com/rango-cfs/NewCollector/refs/heads/main/v2ray_links.txt",
    "https://raw.githubusercontent.com/aqayerez/MatnOfficial-VPN/refs/heads/main/MatnOfficial",
    "https://raw.githubusercontent.com/arshiacomplus/v2rayExtractor/refs/heads/main/mix/sub.html",
    "https://raw.githubusercontent.com/nscl5/5/refs/heads/main/configs/at/all.txt",
    "https://raw.githubusercontent.com/Danialsamadi/v2go/main/All_Configs_Sub.txt",
    "https://raw.githubusercontent.com/HosseinKoofi/GO_V2rayCollector/main/mixed_iran.txt",
    "https://raw.githubusercontent.com/Rayan-Config/C-Sub/refs/heads/main/configs/proxy.txt",
    "https://raw.githubusercontent.com/55prosek-lgtm/vpn_config_for_russia/refs/heads/main/blacklist.txt",
    "https://raw.githubusercontent.com/vlesscollector/vlesscollector/refs/heads/main/vless_configs.txt",
    "https://raw.githubusercontent.com/STR97/STRUGOV/refs/heads/main/Vless#VLESS.BIG.STR.BYPASS%F0%9F%94%A5",
    "https://raw.githubusercontent.com/STR97/STRUGOV/refs/heads/main/STR#MEGA.STR.BYPASS%E2%9A%A1%EF%B8%8F",
    "https://raw.githubusercontent.com/STR97/STRUGOV/refs/heads/main/BYPASS#PROXY.STR.BYPASS%F0%9F%90%BA",
    "https://raw.githubusercontent.com/Kirillo4ka/vpn-configs-for-russia/refs/heads/main/Vless-Rus-Mobile-White-List.txt",
    "https://raw.githubusercontent.com/vsevjik/OBSpiskov/refs/heads/main/wwh",
    "https://raw.githubusercontent.com/EtoNeYaProject/etoneyaproject.github.io/refs/heads/main/1",
    "https://raw.githubusercontent.com/EtoNeYaProject/etoneyaproject.github.io/refs/heads/main/2",
    "https://raw.githubusercontent.com/zieng2/wl/main/vless_universal.txt",
    "https://raw.githubusercontent.com/miladtahanian/multi-proxy-config-fetcher/refs/heads/main/configs/proxy_configs.txt"
]

OUTPUT_DIR = "docs/config/data"
os.makedirs(OUTPUT_DIR, exist_ok=True)

CHROME_UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/138.0.0.0 Safari/537.36"

urllib3.disable_warnings()

logging.basicConfig(level=logging.INFO, format="[%(asctime)s] %(message)s", datefmt="%Y-%m-%d %H:%M:%S")

def b64_decode(s):
    pad = "=" * ((4 - len(s) % 4) % 4)
    try:
        return base64.b64decode(s + pad).decode('utf-8', errors='ignore')
    except:
        return base64.b64decode(s + pad).decode('latin-1', errors='ignore')

def b64_encode(s):
    return base64.b64encode(s.encode()).decode()

def country_flag(code):
    if not code: return "🏳️"
    c = code.strip().upper()
    if len(c) != 2 or not c.isalpha(): return "🏳️"
    return chr(ord(c[0]) + 127397) + chr(ord(c[1]) + 127397)

def get_country_by_ip(ip):
    try:
        r = requests.get(f"https://ipwhois.app/json/{ip}", timeout=3)
        if r.status_code == 200:
            data = r.json()
            return data.get("country_code", "").lower()
    except:
        try:
            r = requests.get(f"https://ipapi.co/{ip}/json/", timeout=3)
            if r.status_code == 200:
                data = r.json()
                return data.get("country_code", "").lower()
        except:
            pass
    return ""

def fetch_data(url, timeout=10):
    headers = {"User-Agent": CHROME_UA}
    try:
        resp = requests.get(url, headers=headers, timeout=timeout, verify=False)
        if resp.status_code == 200:
            content = resp.content
            if b'%' in content[:100]:
                try:
                    return requests.utils.unquote(content.decode('utf-8', errors='ignore'))
                except:
                    pass
            return resp.text
        else:
            logging.warning(f"HTTP {resp.status_code} for {url}")
            return ""
    except Exception as e:
        logging.warning(f"Failed to fetch {url}: {str(e)[:100]}")
        return ""

def maybe_base64_decode(s):
    s = s.strip()
    if not s:
        return s
    try:
        decoded = b64_decode(s)
        if "://" in decoded:
            return decoded.strip()
    except:
        pass
    if s.startswith('http') or "://" in s:
        return s
    return s

def normalize_proto(proto):
    p = proto.lower()
    if p in ("ss", "shadowsocks"): return "shadowsocks"
    if p in ("hy2", "hysteria2"): return "hysteria2"
    if p.startswith("hysteria"): return "hysteria"
    if p == "tuic": return "tuic"
    return p

def detect_protocol(link):
    m = re.match(r"([a-z0-9+.-]+)://", link.strip().lower())
    if not m: return "unknown"
    return normalize_proto(m.group(1))

def split_host_port(raw_hostport):
    raw_hostport = unquote(raw_hostport.strip())
    if "@" in raw_hostport:
        raw_hostport = raw_hostport.split("@", 1)[1]
    if raw_hostport.startswith("["):
        m = re.match(r"^\[(.+?)\](?::(\d+))?$", raw_hostport)
        if m: return m.group(1), (m.group(2) or "443")
    if raw_hostport.count(":") > 1:
        return raw_hostport, "443"
    if ":" in raw_hostport:
        parts = raw_hostport.rsplit(":", 1)
        if len(parts) == 2:
            return parts[0], parts[1]
    return raw_hostport, "443"

def extract_host(link, proto):
    try:
        if proto == "vmess":
            try:
                cfg = json.loads(b64_decode(link.split("://", 1)[1]))
                host = str(cfg.get("add", "")).strip()
                port = str(cfg.get("port", "")).strip()
                if host and port:
                    return f"{host}:{port}"
                return host or ""
            except:
                pass
        if proto == "shadowsocks":
            try:
                body = link.split("ss://", 1)[1]
                if "#" in body:
                    body = body.split("#", 1)[0]
                if "@" in body:
                    _, hostport = body.split("@", 1)
                    return hostport
                decoded = b64_decode(body)
                if "@" in decoded:
                    _, hostport = decoded.split("@", 1)
                    return hostport
                else:
                    parts = decoded.split(":")
                    if len(parts) >= 3:
                        return f"{parts[-2]}:{parts[-1]}"
            except:
                pass
        if proto == "ssr":
            try:
                raw = link.split("ssr://", 1)[1]
                decoded = base64.urlsafe_b64decode(raw + '=' * ((4 - len(raw) % 4) % 4)).decode('utf-8', errors='ignore')
                parts = decoded.split(":")
                if len(parts) >= 2:
                    return f"{parts[0]}:{parts[1]}"
            except:
                pass
        parsed = urlsplit(link)
        netloc = parsed.netloc
        if "@" in netloc:
            netloc = netloc.split("@", 1)[1]
        return netloc
    except Exception as e:
        return ""

_connection_limit = asyncio.Semaphore(15)

async def run_ping_once(client, host, timeout=30, retries=2):
    if not host or len(host) > 100:
        return {}
    base = "https://check-host.net"
    async with _connection_limit:
        for attempt in range(retries):
            try:
                r1 = await client.get(
                    f"{base}/check-ping",
                    params={"host": host.split(":")[0]},
                    headers={"Accept": "application/json"},
                    timeout=timeout
                )
                if r1.status_code in (429, 503):
                    await asyncio.sleep(random.uniform(2, 5))
                    continue
                r1.raise_for_status()
                j1 = r1.json()
                req_id = j1.get("request_id")
                if not req_id:
                    continue
                await asyncio.sleep(3)
                for _ in range(15):
                    await asyncio.sleep(2)
                    try:
                        r2 = await client.get(
                            f"{base}/check-result/{req_id}",
                            headers={"Accept": "application/json"},
                            timeout=timeout
                        )
                        if r2.status_code in (429, 503):
                            await asyncio.sleep(3)
                            continue
                        r2.raise_for_status()
                        data = r2.json()
                        if data:
                            has_ok = False
                            for entries in data.values():
                                if isinstance(entries, list) and entries:
                                    first = entries[0]
                                    if isinstance(first, list):
                                        for row in first:
                                            if isinstance(row, list) and row and row[0] == "OK":
                                                has_ok = True
                                                break
                                if has_ok:
                                    break
                            if has_ok:
                                return data
                    except:
                        continue
            except Exception:
                await asyncio.sleep(1)
    return {}

def extract_latency_global(results):
    pings = []
    for entries in (results or {}).values():
        if isinstance(entries, list) and entries:
            first = entries[0]
            if isinstance(first, list):
                for row in first:
                    if isinstance(row, list) and row and row[0] == "OK" and len(row) >= 2:
                        try:
                            pings.append(float(row[1]))
                        except:
                            pass
    return (sum(pings) / len(pings)) if pings else float("inf")

def latencies_by_cc_from_results(results):
    pings_by_cc = defaultdict(list)
    for node, entries in (results or {}).items():
        node_base = node.split("/")[0].split(":")[0].split(".")[0].lower()
        cc = node_base[:2] if len(node_base) >= 2 else ""
        if not cc or not cc.isalpha():
            continue
        if isinstance(entries, list) and entries:
            first = entries[0]
            if isinstance(first, list):
                for row in first:
                    if isinstance(row, list) and row and row[0] == "OK" and len(row) >= 2:
                        try:
                            pings_by_cc[cc].append(float(row[1]))
                        except:
                            pass
    return {cc: (sum(v)/len(v)) if v else float("inf") for cc, v in pings_by_cc.items()}

def save_to_file(path, lines):
    if not lines:
        return
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    logging.info(f"Saved: {path} ({len(lines)} lines)")

def rename_vmess(link, ip, port, tag):
    try:
        raw = link.split("://", 1)[1]
        cfg = json.loads(b64_decode(raw))
        cfg["add"] = ip
        cfg["port"] = int(port) if port else 443
        cfg["ps"] = tag
        new_b64 = b64_encode(json.dumps(cfg, ensure_ascii=False, separators=(',', ':')))
        return f"vmess://{new_b64}#{quote(tag)}"
    except:
        return link

def rename_shadowsocks(link, ip, port, tag):
    try:
        body = link.split("ss://", 1)[1]
        if "#" in body:
            body = body.split("#", 1)[0]
        method = pwd = None
        if "@" in body:
            creds_part, hostport = body.split("@", 1)
            try:
                method, pwd = b64_decode(creds_part).split(":", 1)
            except:
                try:
                    method, pwd = creds_part.split(":", 1)
                except:
                    return link
        else:
            try:
                decoded = b64_decode(body)
                if "@" in decoded:
                    creds, hostport = decoded.split("@", 1)
                    method, pwd = creds.split(":", 1)
                else:
                    parts = decoded.split(":")
                    if len(parts) >= 3:
                        method, pwd = parts[0], parts[1]
            except:
                return link
        if not method or not pwd:
            return link
        new_creds = b64_encode(f"{method}:{pwd}")
        hp = f"[{ip}]:{port}" if ":" in ip else f"{ip}:{port}"
        return f"ss://{new_creds}@{hp}#{quote(tag)}"
    except:
        return link

def rename_line(link):
    proto = detect_protocol(link)
    host_port = extract_host(link, proto)
    if not host_port:
        return link
    host, port = split_host_port(host_port)
    if not port or not port.isdigit():
        port = "443"
    
    try:
        if re.match(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$', host):
            ip = host
        elif re.match(r'^[0-9a-fA-F:]+$', host):
            ip = host
        else:
            ip = socket.gethostbyname(host)
    except:
        ip = host
    
    country = get_country_by_ip(ip.split(":")[0] if ":" in ip else ip)
    flag = country_flag(country)
    tag = f"{flag} WorDa {random.randint(10000, 99999)}"
    
    if proto == "vmess":
        return rename_vmess(link, ip, port, tag)
    elif proto == "shadowsocks":
        return rename_shadowsocks(link, ip, port, tag)
    else:
        try:
            parsed = urlsplit(link)
            netloc = parsed.netloc
            hp = f"[{ip}]:{port}" if ":" in ip else f"{ip}:{port}"
            if "@" in netloc:
                userinfo, _ = netloc.split("@", 1)
                new_netloc = f"{userinfo}@{hp}"
            else:
                new_netloc = hp
            return urlunsplit((parsed.scheme, new_netloc, parsed.path, parsed.query, quote(tag)))
        except:
            return link

def group_by_protocol(links):
    out = {}
    for l in links:
        proto = detect_protocol(l)
        out.setdefault(proto, []).append(l)
    return out

async def main_async():
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    logging.info(f"[{now}] Starting WorDa config update...")
    
    all_links = []
    for url in URLS:
        try:
            content = fetch_data(url)
            if not content:
                continue
            
            decoded = maybe_base64_decode(content)
            links = re.findall(r'[a-zA-Z][\w+.-]*://[^\s<>"\'\[\](){}]+', decoded)
            
            if not links and "://" in decoded:
                links = [decoded]
            
            valid_links = []
            for link in links:
                link = link.strip()
                if link and len(link) < 1000 and "://" in link:
                    valid_links.append(link)
            
            logging.info(f"Fetched {url}: {len(valid_links)} links")
            all_links.extend(valid_links)
            
        except Exception as e:
            logging.warning(f"Error processing {url}: {str(e)[:100]}")
    
    if not all_links:
        logging.warning("No links found")
        return
    
    all_links = list(set(all_links))
    logging.info(f"Total unique links: {len(all_links)}")
    
    host_to_links = defaultdict(list)
    for link in all_links:
        proto = detect_protocol(link)
        host_port = extract_host(link, proto)
        if host_port:
            host, _ = split_host_port(host_port)
            if host:
                host_to_links[host].append(link)
    
    hosts = list(host_to_links.keys())
    logging.info(f"Unique hosts: {len(hosts)}")
    
    async with httpx.AsyncClient(timeout=30) as client:
        tasks = [run_ping_once(client, h) for h in hosts]
        ping_results = await asyncio.gather(*tasks, return_exceptions=True)
    
    results_by_host = {}
    for host, result in zip(hosts, ping_results):
        if isinstance(result, dict):
            results_by_host[host] = result
        else:
            results_by_host[host] = {}
    
    host_global_lat = {}
    for host in hosts:
        host_global_lat[host] = extract_latency_global(results_by_host.get(host, {}))
    
    link_global_lat = {}
    for host, links in host_to_links.items():
        lat = host_global_lat.get(host, float("inf"))
        for link in links:
            current = link_global_lat.get(link, float("inf"))
            if lat < current:
                link_global_lat[link] = lat
    
    sorted_global_links = [l for l, _ in sorted(link_global_lat.items(), key=lambda x: x[1])]
    
    global_dir = os.path.join(OUTPUT_DIR, "global")
    os.makedirs(global_dir, exist_ok=True)
    
    renamed_global = [rename_line(l) for l in sorted_global_links[:5000]]
    save_to_file(os.path.join(global_dir, "all.txt"), renamed_global)
    save_to_file(os.path.join(global_dir, "light.txt"), renamed_global[:100])
    
    grouped_global = group_by_protocol(sorted_global_links[:5000])
    for proto in ["vless", "vmess", "shadowsocks", "trojan", "hysteria", "hysteria2", "tuic"]:
        proto_links = grouped_global.get(proto, [])
        renamed = [rename_line(l) for l in proto_links[:1000]]
        save_to_file(os.path.join(global_dir, f"{proto}.txt"), renamed)
    
    countries = ["us", "gb", "de", "fr", "jp", "sg", "ru", "ir", "cn", "kr", "tr", "in", "br", "ca", "au", "nl", "ch", "se", "no", "fi", "dk", "pl", "cz", "hu", "at", "it", "es", "pt", "gr", "il", "sa", "ae", "qa", "om", "kw", "bh", "az", "ge", "am", "kz", "uz", "tm", "kg", "tj", "af", "pk", "bd", "lk", "np", "bt", "mv", "id", "my", "th", "vn", "ph", "mm", "la", "kh", "mx", "co", "pe", "cl", "ar", "uy", "py", "bo", "ec", "ve", "za", "eg", "ma", "dz", "tn", "ly", "sd", "et", "ke", "tz", "ug", "rw", "ng", "gh"]
    
    for country in countries:
        logging.info(f"Processing country: {country}")
        
        link_country_lat = {}
        for host, links in host_to_links.items():
            per_cc = latencies_by_cc_from_results(results_by_host.get(host, {}))
            lat = per_cc.get(country, float("inf"))
            if lat == float("inf"):
                lat = host_global_lat.get(host, float("inf"))
            
            for link in links:
                current = link_country_lat.get(link, float("inf"))
                if lat < current:
                    link_country_lat[link] = lat
        
        sorted_links = [l for l, lat in sorted(link_country_lat.items(), key=lambda x: x[1]) if lat < float("inf")]
        
        if not sorted_links:
            continue
        
        dest_dir = os.path.join(OUTPUT_DIR, country)
        os.makedirs(dest_dir, exist_ok=True)
        
        renamed_country = [rename_line(l) for l in sorted_links[:1000]]
        save_to_file(os.path.join(dest_dir, "all.txt"), renamed_country)
        save_to_file(os.path.join(dest_dir, "light.txt"), renamed_country[:50])
        
        grouped_country = group_by_protocol(sorted_links[:1000])
        for proto in ["vless", "vmess", "shadowsocks", "trojan"]:
            proto_links = grouped_country.get(proto, [])
            renamed = [rename_line(l) for l in proto_links[:200]]
            save_to_file(os.path.join(dest_dir, f"{proto}.txt"), renamed)
    
    logging.info("Config update completed!")

if __name__ == "__main__":
    asyncio.run(main_async())
